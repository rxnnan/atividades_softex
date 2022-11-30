import {useState} from 'react';

export const Segunda = function Contador() {
    const [i, contagem] = useState(0);

    return (
        <>
            <button onClick={()=> contagem(i+1)}>
                Clique aqui!
            </button>
            <p>O botão foi clicado {i} vezes.</p>
        </>
    )
}

