import React, {useState} from 'react';
import {useLocation} from 'react-router-dom';
import general_pic from "./pictures/general-pic.jpg";
import GeneralLineTable from "./GeneralLineTable"
import FindForParamsForm from "./FindForParamsForm"
import CarsTable from "./CarsTable"


const SelectedCarMarkPage = ({generalItems, cars, models}) => {

    const location = useLocation();
    const [mark, setMark] = useState(generalItems.filter(t => t.title === location.state.selectedMark))
    const [markLink, setMarkLink] = useState(location.state.link)
    const [modelLink, setModelLink] = useState("")
    const [selectedCars, setSelectedCars] = useState(cars.filter(car => car.mark_link === location.state.link))
    const [carsCount, setCarsCount] = useState(location.state.count)
    const [yearFrom, setYearFrom] = useState(null)
    const [yearTo, setYearTo] = useState(null)

    const handleMarkCount = (markCount) => {
        setCarsCount(markCount)
        }

    const handleChangeMark = (markLink) => {
        setMarkLink(markLink)
        setSelectedCars(cars.filter(car => car.mark_link === markLink))

  }

   const handleChangeModel = (modelLink) => {
        setModelLink(modelLink)
        setSelectedCars(cars.filter(car => car.model_link === modelLink))
    }

    const handleChangeYearFrom = (year) => {
        setYearFrom(Number(year))
         if (markLink !== "" && modelLink !== "" && yearTo !== null) {
             setSelectedCars(cars.filter(car => car.model_link === modelLink && car.mark_link === markLink && car.year >= year && car.year <= yearTo))
             }else if(markLink !== "" && modelLink === "" && yearTo !== null){
                 setSelectedCars(cars.filter(car => car.mark_link === markLink && car.year >= year && car.year <= yearTo))
             }else if(markLink === "" && modelLink === "" && yearTo === null){
                 setSelectedCars(cars.filter(car => car.year >= year))
             }else if(markLink === "" && modelLink === "" && yearTo !== null){
                 setSelectedCars(cars.filter(car => car.year >= year && car.year <= yearTo))
             }else if(markLink !== "" && modelLink !== "" && yearTo === null){
                 setSelectedCars(cars.filter(car => car.model_link === modelLink && car.mark_link === markLink && car.year >= year))
             }else if (markLink !== "" && modelLink === "" && yearTo === null){
                 setSelectedCars(cars.filter(car => car.mark_link === markLink && car.year >= year))
                 }
    }

    const handleChangeYearTo = (year) => {
        setYearTo(Number(year))
        if (markLink !== "" && modelLink !== "" && yearFrom !== null) {
             setSelectedCars(cars.filter(car => car.model_link === modelLink && car.mark_link === markLink && car.year >= yearFrom && car.year <= year))
             }else if (markLink !== "" && modelLink !== "" && yearFrom === null){
                 setSelectedCars(cars.filter(car => car.model_link === modelLink && car.mark_link === markLink && car.year <= year))
             }else if (markLink !== "" && modelLink === "" && yearFrom !== null){
                 setSelectedCars(cars.filter(car => car.mark_link === markLink && car.year >= yearFrom && car.year <= year))
             }else if (markLink === "" && yearFrom === null){
                 setSelectedCars(cars.filter(car => car.year <= year))
             }else if (markLink === "" && yearFrom !== null){
                 setSelectedCars(cars.filter(car => car.year >= yearFrom && car.year <= year))
             }else if (markLink !== "" && modelLink === "" && yearFrom === null){
                 setSelectedCars(cars.filter(car => car.mark_link === markLink && car.year <= year))
                 }

}

    if (location.state.count===0) {
        return(
            <div>
            <img className="general-pic" src={general_pic} alt="fish"/>
                <GeneralLineTable/>
            <h3> Нет доступных моделей </h3>
            </div>
        )
    }

    return(
        <div>
            <img className="general-pic" src={general_pic} alt="fish"/>
            <GeneralLineTable/>
            <FindForParamsForm changedYearFrom={handleChangeYearFrom} changedYearTo={handleChangeYearTo}
                               changedModelLink={handleChangeModel} changedMarkLink={handleChangeMark}
                               changedMarkCount={handleMarkCount} carsCount={carsCount} defaultCount={location.state.count}
                               defaultValue={mark} defaultValueId={location.state.id} models={models}
                               generalItems={generalItems} cars={cars}/>
            <div></div>
            <div>My link is:{markLink}</div>
            <div>My count is:{location.state.count}</div>
            <div>My count is:{location.state.id}</div>
            <div>My id is:{location.state.selectedMark}</div>
            <tr class="tr-car-item">
                 <CarsTable carsCount={carsCount} cars={selectedCars}/>
            </tr>

            </div>


        )}


export default SelectedCarMarkPage;