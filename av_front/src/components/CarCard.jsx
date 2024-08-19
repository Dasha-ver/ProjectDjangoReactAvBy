import React from "react";
import CarouselComponent from "./CarouselComponent.jsx";

const CarCard = (props) => {

    let img = props.carCard.image_links.split(/,/)

    return(
         <div>
            <strong>{props.carCard.id}</strong>
            <strong>{img[1]}</strong>
            <div>
                <CarouselComponent img={img}/>
            </div>
        </div>
    )
}

export default CarCard;

