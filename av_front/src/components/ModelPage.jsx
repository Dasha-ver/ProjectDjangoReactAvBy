import React from "react" ;
import Model from "./Model"

const ModelPage= ({models}) => {

    if (!models.length) {
        return <h3> Нет информации </h3>
    }

    return(
    <div>
        {models.map(model => <Model model={model} key={model.id}/>)}
    </div>
    )
}

export default ModelPage;