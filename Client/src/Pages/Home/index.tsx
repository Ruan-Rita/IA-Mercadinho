import { log } from 'console'
import React, { MouseEventHandler, useState } from 'react'
import {Container, SideBar ,Graph,Content, Node,NodeFather, MSG} from "./styles"

const Home : React.FC =  () => {
    const [method, setMethod ] = useState<string>("amplitude")
    const [input, setInput ] = useState<string>("A")
    const [output, setOutput ] = useState<[string]>([""])
    const [limit, setLimit ] = useState<string>("3")

    const [msgFeedback, setMsgFeedback] = useState("")

    const [node, setNode] = useState([
        ["A", "1", "0", "#966493","0"], 
        ["B", "4", "0", "#966493","0"], 
        ["C", "3", "1", "#966493","0"], 
        ["D", "5", "1", "#966493","0"], 
        ["E", "0", "2", "#966493","0"], 
        ["F", "0", "3", "#966493","0"], 
        ["G", "1", "4", "#966493","0"], 
        ["H", "2", "4", "#966493","0"], 
        ["I", "3", "4", "#966493","0"], 
        ["J", "4", "4", "#966493","0"], 
        ["K", "0", "5", "#966493","0"], 
        ["L", "1", "6", "#966493","0"], 
        ["M", "2", "6", "#966493","0"], 
        ["N", "3", "6", "#966493","0"], 
        ["O", "3", "7", "#966493","0"]
    ])
    const nodeFill = [ 
        ["0","0"], ["0", "1"], ["0", "2"], ["0", "3"], ["0", "4"], ["0", "5"], ["0", "6"], ["0", "7"], 
        ["1","0"], ["1", "1"], ["1", "2"], ["1", "3"], ["1", "4"], ["1", "5"], ["1", "6"], ["1", "7"], 
        ["2","0"], ["2", "1"], ["2", "2"], ["2", "3"], ["2", "4"], ["2", "5"], ["2", "6"], ["2", "7"], 
        ["3","0"], ["3", "1"], ["3", "2"], ["3", "3"], ["3", "4"], ["3", "5"], ["3", "6"], ["3", "7"], 
        ["4","0"], ["4", "1"], ["4", "2"], ["4", "3"], ["4", "4"], ["4", "5"], ["4", "6"], ["4", "7"], 
        ["5","0"], ["5", "1"], ["5", "2"], ["5", "3"], ["5", "4"], ["5", "5"], ["5", "6"], ["5", "7"], 
    ]
    const verifyItem = (item: Array<string>) => {
        const letter = node.find(letter => letter[1] === item[0] && letter[2] === item[1])
        if(letter?.length) return letter
        else return [] 
    }
    const changeColorItem = (caminho: [string]) => {
        const aux = node.map(item => {
            caminho.forEach((element, index) => {
                let color = "#e2d62c"
                if(caminho[caminho.length -1] == element) color= "#e2502c"
                else if(caminho[0] == element) color = "#2ce22c"
                
                if(item[0] === element) {
                    item[3] = color
                }
            });
            return item;
        })
        setNode(aux)
    }
    const getWay = () => {
        
        resetColorsMsg()
        console.log("TESTe")
        console.log(input, output,method,limit);
        
        const params = new FormData();
        params.append("input", input)
        params.append("output", JSON.stringify(output))
        params.append("method", method)
        params.append("limit", limit)
        
       
        const url = 'http://localhost:5000/way-search';
        const options = {
            url:"http://localhost:5000/way-search",
            method: 'POST',
            body: params
        };
        fetch(url, options).then(response => response.json())
        .then(data => {
            console.log("data")
            console.log(data)
            if (typeof data === 'string' || data instanceof String){
                setMsgFeedback(String(data))
                setTimeout(() => {
                    setMsgFeedback("")
                }, 3000)
            }else{
                if(method === "estrela" || method === "greedy" || method === "custo-uniforme"  ){
                    changeColorItem(data[0])
                    setMsgFeedback(`Custo: ${data[1]}`)

                    
                }else{
                    changeColorItem(data)
                }
                
            }
            
            
        })
        

    }
    const resetColorsMsg = ()=> {
        setMsgFeedback("")
        const aux = node.map(item => {
            item[3] = "#966493"
            return item;
        })
        setNode(aux)
    }
    const verifyOutputhtml = (element: string) => {
        let validate = null;
        var auxOutput = output
        auxOutput.forEach((item, index) => {
            if(item == element){
                validate = true;
                auxOutput.splice(index, 1)
            }else if(item == ""){
                auxOutput.splice(index, 1)
            }
        })
        if(!validate) auxOutput.push(element)
        setOutput(auxOutput)
    }
    
    return (
        <Content>
            <SideBar onSubmit={event => {
                event.preventDefault()
                getWay();
            }}>
                <h1>SuperMercado</h1>
                <div>
                    <label>Selecionar Metodo: </label>
                    <select name="method" required onChange={event => setMethod(String(event.target.value))}>
                        <option value="amplitude" selected >Amplitude</option>
                        <option value="profundidade" >Profundidade</option>
                        <option value="profundidade-limitada" >Profundidade Limitada</option>
                        <option value="aprofundamento" >Aprofundamento</option>
                        <option value="bidirecional" >Bidirecional</option>
                        <option value="estrela" >Estrela</option>
                        <option value="greedy" >Greedy</option>
                        <option value="custo-uniforme" >Custo Uniforme</option>
                    </select>
                </div>
                <div>
                    <label>Selecionar Entrada:</label>
                    <select name="input" required onChange={event => setInput(String(event.target.value))}>
                        {node.map((item, index) => (
                            <option key={index} {...item[0] === input ? "selected" : ""}>{item[0]}</option>
                        ))}
                    </select>
                </div>
                <div>
                    <label>Selecionar Saida:</label>
                    <div>
                        {node.map((item, index) => (
                            <label key={index}><input key={index} onChange={event => verifyOutputhtml(event.target.value)} name="output" type="checkbox" value={item[0]} />{item[0]}</label>
                        ))}
                    </div>
                </div>
                <div>
                    <label>Digite o limite:</label>
                    <input name="limit" onChange={event => setLimit(String(event.target.value))} type="text" placeholder="Informe um numero" value={limit} />
                </div>
                <div>
                    {/* <button onClick={event => handleClickForm(event)}>Procurar Caminho</button> */}
                    <button>Procurar Caminho</button>
                </div>
            </SideBar>
            <Container>
                {msgFeedback != "" && (
                    <MSG background={`#ff2929f5`} >
                        {msgFeedback}
                    </MSG>
                ) }
                <Graph>
                    
                    {nodeFill.map((item, index) => 
                        <NodeFather key={index}>
                            <Node key={index} background={verifyItem(item)[0] ? verifyItem(item)[3]:"#966493"} className={`${!verifyItem(item)[0] && "no-item"}`} >
                                {verifyItem(item) && (verifyItem(item)[0])}
                            </Node>
                        </NodeFather>
                    )}

                </Graph>
            </Container>
        </Content>

    )
}
export default Home;
