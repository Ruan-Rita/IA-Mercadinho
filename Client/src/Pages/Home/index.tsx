import React from 'react'
import {Container, SideBar ,Graph,Content, Node, Connector, NodeFather} from "./styles"

const Home : React.FC =  () => {
    const node = [ ["A", "1", "0"], ["B", "4", "0"], ["C", "3", "1"], ["D", "5", "1"], ["E", "0", "2"], ["F", "0", "3"], ["G", "1", "4"], ["H", "2", "4"], ["I", "3", "4"], ["J", "4", "4"], ["K", "0", "5"], ["L", "1", "6"], ["M", "2", "6"], ["N", "3", "6"], ["O", "3", "7"]]
    const nodeFill = [ 
        ["0","0"], ["0", "1"], ["0", "2"], ["0", "3"], ["0", "4"], ["0", "5"], ["0", "6"], ["0", "7"], 
        ["1","0"], ["1", "1"], ["1", "2"], ["1", "3"], ["1", "4"], ["1", "5"], ["1", "6"], ["1", "7"], 
        ["2","0"], ["2", "1"], ["2", "2"], ["2", "3"], ["2", "4"], ["2", "5"], ["2", "6"], ["2", "7"], 
        ["3","0"], ["3", "1"], ["3", "2"], ["3", "3"], ["3", "4"], ["3", "5"], ["3", "6"], ["3", "7"], 
        ["4","0"], ["4", "1"], ["4", "2"], ["4", "3"], ["4", "4"], ["4", "5"], ["4", "6"], ["4", "7"], 
        ["5","0"], ["5", "1"], ["5", "2"], ["5", "3"], ["5", "4"], ["5", "5"], ["5", "6"], ["5", "7"], 
    ]
    const verifyItem = (item: Array<string>) => {
        let letterCustom = "";
        // let result = {result :false, letter: null, with: null, rotate: null}
        const letter = node.filter(letter => {
            if(letter[1] === item[0] && letter[2] === item[1] ) {
                letterCustom = letter[0]
                return letter[0]
            }
        })
        
        
        if(letterCustom != "") {
            return letterCustom
        
        }

        else return false 
    }
    return (
        <Content>
            <SideBar>
                <h1>SuperMercado</h1>
                <div>
                    <label>Selecionar Metodo:</label>
                    <select>
                        <option selected>Amplitude</option>
                        <option>Amplitude</option>
                        <option>Amplitude</option>
                        <option>Amplitude</option>
                    </select>
                </div>
                <div>
                    <label>Selecionar Entrada:</label>
                    <select>
                        <option selected>Amplitude</option>
                        <option>Amplitude</option>
                        <option>Amplitude</option>
                        <option>Amplitude</option>
                    </select>
                </div>
                <div>
                    <label>Selecionar Saida:</label>
                    <div>
                        <label><input type="checkbox" value="20" />A</label>
                        <label><input type="checkbox" value="20" />B</label>
                        <label><input type="checkbox" value="20" />C</label>
                        <label><input type="checkbox" value="20" />D</label>
                        <label><input type="checkbox" value="20" />E</label>
                    </div>
                </div>
                <div>
                    <label>Digite o limite:</label>
                    <input type="text" placeholder="Informe um numero" />
                </div>
                <div>
                    <button>Procurar Caminho</button>
                </div>
            </SideBar>
            <Container>
                <Graph>
                    {
                        nodeFill.map((item, index) => 
                            <NodeFather>
                                <Node className={`${!verifyItem(item) && "no-item"}`} key={index}>
                                    {verifyItem(item) && (verifyItem(item))}
                                </Node>
                                {verifyItem(item) && (
                                    <Connector widthProps="160px" rotateProps="152deg" />
                                )}
                            </NodeFather>
                        )
                    }
                </Graph>
            </Container>
        </Content>

    )
}
export default Home;
