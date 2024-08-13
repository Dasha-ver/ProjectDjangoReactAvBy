import React from "react" ;
import CheckedCar from "./CheckedCar"

const CheckedCarPage = ({checkedCars}) => {

    if (!checkedCars.length) {
        return <h3> Нет информации </h3>
    }

    return(
    <div>
        {checkedCars.map(checkedCar => <CheckedCar checkedCar={checkedCar} key={checkedCar.id}/>)}
    </div>
    )
}

export default CheckedCarPage;