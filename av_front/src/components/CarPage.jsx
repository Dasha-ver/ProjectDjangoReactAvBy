import React from "react" ;
import Car from "./Car"

const CarPage= ({cars}) => {

    if (!cars.length) {
        return <h3> Нет информации </h3>
    }

    return(
    <div>
        {cars.map(car => <Car car={car} key={car.id}/>)}
         </div>
    )
}

export default CarPage;