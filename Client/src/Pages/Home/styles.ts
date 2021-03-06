import styled from "styled-components"
export const Content = styled.div`
    width: 100%;
    min-height: 100vh;
    background-color: azure;
    display: grid;
    grid-template-columns: 350px 1fr;
`

export const Container = styled.div`
    display: flex;
    align-items: center;
    flex-direction: column;
    padding: 35px;
    position: relative;

`
interface IMSG{
    background: string
}
export const MSG = styled.div<IMSG>`
    width: 930px;
    padding: 15px 0px;
    max-height: 70px;
    display: flex;
    align-items: center;
    justify-content: center;
    position: fixed;
    color: white;
    font-weight: 600;
    z-index: 999;
    border-radius:20px;
    transform: translate(0%, -70%);
    background-color: ${props => props.background};
`
export const SideBar = styled.form`
    background-color:#b8d59670 ;
    height: 100%;
    display: flex;
    align-items: center;
    border-right: 1px solid black;
    flex-direction: column;
    padding: 20px;
    h1{
        color: #2d5a28;
        margin-bottom: 20px;
        
    }
    > div{
        width: 100%;
        display: flex;
        margin: 10px 0px;
        
        flex-direction: column;
        &:last-child{
            margin-top: auto;
        }
        > div{
            display: flex;
            justify-content: flex-start;
            flex-wrap: wrap;
            label{
                margin: 10px;
            }
        }
        label{
            font-size: 1.5rem;
            color: #005a00;
            display: flex;
            align-items: center;
            input{
                width: 30px;
                height: 30px;
                margin-right: 10px;
            }
        }
        select, input{
            margin-top: 5px;
            font-size: 1.5rem;
            padding: 5px 10px;
            border: 1px solid #0ce10c;
            border-radius: 5px;
            background: #578b57e3;
            color: #ffffff;

            &::placeholder{
                color: #ffffff;

            }
        }
        button{
            background: #0cd90ce3;
            color: #ffffff;

            font-size: 1.6rem;
            padding: 10px;
            border-radius: 8px;
            border: 1px solid #0ce10c;
            /* box-shadow: 1px 1px 14px -4px #044e04; */
            cursor: pointer;
        }
    }
    

`
interface IGraph{
    image: string;
}
export const Graph = styled.div<IGraph>`
    width: 877px !important;
    max-height: 524px !important;
    background-image: url(${props => props.image});
    background-repeat: no-repeat;
    background-size: contain;
    flex: 1;
    /* margin-top: 20px; */
    border-radius: 10px;
    padding: 10px;
    width: 100%;
    background-color: rgba(10,10,10,0.1);
    height: calc(100% -30px);
    display: grid;
    grid-template-columns: calc(100% / 8) calc(100% / 8) calc(100% / 8) calc(100% / 8) calc(100% / 8) calc(100% / 8)  calc(100% / 8)  calc(100% / 8) ;
    grid-template-rows: calc(100% / 6) calc(100% / 6) calc(100% / 6) calc(100% / 6) calc(100% / 6) calc(100% / 6);

    /* gap: 30px; */

`
export const NodeFather = styled.div`
    position: relative;
    width: 100%;

`
interface IConnector{
    widthProps: string,
    rotateProps: string
}

export const Connector = styled.div<IConnector>`
    background: green;
    /* float: left; */
    position: absolute;
    width: ${props => props.widthProps};
    height: 10px;
    top: -3px;
    left: 61%;
    transform: ${props => `rotate(${props.rotateProps})`};
`
interface INode{
    background: string;
    content: string;
    displayAfter: string;
}
export const Node = styled.div<INode>`
    width: 60px;
    position: relative;
    border-radius: 50%;
    height: 60px;
    margin: 10px;
    background-color: ${props => props.background};
    color: white;
    z-index: 100;
    display: flex;
    justify-content: center;
    align-items: center;

    &.no-item{
        background: rgba(300, 20, 20, 0);
        &:after{
            display:none !important;
        }
    }
    
    &:after{
        /* ${props =>  props.content !== '' && 'content:' + props.content+";"  }; */
        display: ${props =>  props.displayAfter} !important;
        content: "${props =>  props.content}";
        width: 25px;
        height: 25px;
        color: #1f1846e3 ;
        display: flex;
        justify-content: center;
        align-items: center;
        background: rgb(103 206 229);
        border:1px solid white;
        border-radius: 25px;
        padding: 5px;
        top: 0px;
        right: 0px;
        transform: translate(0%, -50%);
        position:absolute;
    }
    
`