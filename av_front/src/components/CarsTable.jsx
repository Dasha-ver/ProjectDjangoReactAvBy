import React, {useState} from 'react';
import Car from "./Car";
import GeneralItem from "./GeneralItem"

const CarsTable = ({cars, carsCount}) => {

return(
    <div>

        <table class="cars-table">
            <tr class="tr-find-number-of-ads">
                <td class="td-find-number-of-ads">
                        Найдено {carsCount} объявлений
                    </td>
                    <td class="td-find-number-of-ads-btn">
                        <button class="btn-find-number-of-ads">Сначала актуальные</button>
                        </td>
                </tr>



            </table>
                <tr class="tr-car-item">

                     {cars.map(car => <Car car={car} key={car.id}/>)}

                    </tr>
                    </div>

    )



}

export default CarsTable;
