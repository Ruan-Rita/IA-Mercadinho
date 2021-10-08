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

`
export const SideBar = styled.div`
    background-color:#b8d59670 ;
    height: 100%;
    display: flex;
    align-items: center;
    border-right: 1px solid black;
    flex-direction: column;
    padding: 20px;
    h1{
        color: #222;
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
export const Graph = styled.div`
    flex: 1;
    margin-top: 20px;
    border-radius: 10px;
    padding: 10px;
    width: 100%;
    background-color: rgba(10,10,10,0.1);
    height: calc(100% -30px);
    display: grid;
    grid-template-columns: calc(100% / 6) calc(100% / 6) calc(100% / 6) calc(100% / 6) calc(100% / 6) calc(100% / 6) ;
    grid-template-rows: calc(100% / 6) calc(100% / 6) calc(100% / 6) calc(100% / 6) calc(100% / 6) calc(100% / 6);

    /* gap: 30px; */

`
export const Title = styled.div`
    font-size: 2.5rem;
    color: #222;
    text-align: center;

`
export const Node = styled.div`
    width: 70px;
    border-radius: 50%;
    height: 70px;
    margin: 10px;
    background-color: #966493;
    color: white;

    display: flex;
    justify-content: center;
    align-items: center;

    &.no-item{
        background: rgba(300, 20, 20, 0.2);
    }
`