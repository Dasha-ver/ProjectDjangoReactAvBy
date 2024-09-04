import React from "react";
import CarouselComponent from "./CarouselComponent.jsx";

const CarCard = (props) => {

    let img = props.carCard.image_links.split(/,/)

    return(
         <div class="car-card-item">
         <table class="car-card-item-table">
            <div class="J">{props.carCard.card_header}</div>
            <div class="K">добавлено {props.carCard.date_added}</div>
            <div class="L"><CarouselComponent class="carousel-component" img={img}/></div>
            <div class="M">
                <div class="car-card-price-primary">{props.carCard.card_price_primary} p.</div>
                <div class="car-card-price-secondary">≈ {props.carCard.card_price_secondary} $</div>
                <div class="car-card-commercial">{props.carCard.card_commercial}</div>
            </div>
            <div class="N"></div>
            <div class="O"></div>
            <div class="P"></div>
            <div class="R"></div>
        </table>

        </div>
    )
}

export default CarCard;

