import React from "react";

const CheckedCar = (props) => {

    return(

         <div>
            <strong>{props.checkedCar.car}</strong>
            <strong>{props.checkedCar.id}</strong>
        </div>
    )
}

export default CheckedCar;

