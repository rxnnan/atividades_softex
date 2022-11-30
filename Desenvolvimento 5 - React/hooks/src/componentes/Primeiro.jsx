import {useState} from 'react';

export const Msg = props => <h1>Desenvolimento feito por {props.nome}.</h1>

export const Cont = function Contador() {
    const [i, contagem] = useState(0);

    return (
        <>
            <hr />
            <button onClick={()=> contagem(i+1)}>
                Clique aqui!
            </button>
            <p>O botão foi clicado {i} vezes.</p>
        </>
    )
}

