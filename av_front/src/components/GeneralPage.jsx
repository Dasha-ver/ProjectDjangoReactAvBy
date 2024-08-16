import React, {useState} from "react" ;
import general_pic from "../pictures/general-pic.jpg";
import FindForParamsForm from "./FindForParamsForm"
import GeneralPageItemsTable from "./GeneralPageItemsTable"
import SecondAd from "./SecondAd"
import GeneralLineTable from "./GeneralLineTable"
import CarsTable from "./CarsTable"
import axios from "axios"


const GeneralPage= ({generalItems, cars, models}) => {

    const [selectedCars, setSelectedCars] = useState([])
    const [carsCount, setCarsCount] = useState('')
    const [mark, setMark] = useState('')
    const [model, setModel] = useState('')
    const [yearFrom, setYearFrom] = useState('')
    const [yearTo, setYearTo] = useState('')
    const [priceFrom, setPriceFrom] = useState(0)
    const [priceTo, setPriceTo] = useState(10000000)
    const [currency, setCurrency] = useState('USD')

    async function getSelectedCars(selected) {
        const response = await axios.get("http://127.0.0.1:8000/" + selected)
        setSelectedCars(response.data)
    }

    const handleCarsCount = (carsCount) => {
        setCarsCount(carsCount)
    }

    const handleChangeMark = (mark) => {
        setMark(mark)
        setModel('')
        getSelectedCars('cars/?mark_link_text__in='+mark)
    }

   const handleChangeModel = (model) => {
       getSelectedCars('cars/?mark_link_text__in='+mark+'&model_link_text__in='+model)
       setModel(model)
   }

    const handleChangeYearFrom = (year) => {
        setYearFrom(year)
         if (mark !== "" && model === "" && yearTo === ""){
             getSelectedCars('cars/?mark_link_text__in='+mark+'&year__gte='+year)
              }else if ( mark !== "" && model !== "" && yearTo === ""){
                  getSelectedCars('cars/?mark_link_text__in='+mark+'&model_link_text__in='+model+'&year__gte='+year)
              }else if( mark !== "" && model === "" && yearTo !== ""){
                  getSelectedCars('cars/?mark_link_text__in='+mark+'&year__range='+year+','+yearTo)
              }else if(mark === "" && model === "" && yearTo === ""){
                  getSelectedCars('cars/?year__gte='+year)
              }else if ( mark === "" && model === "" && yearTo !== ""){
                  getSelectedCars('cars/?year__range=' + year + ',' + yearTo)
              }else if( mark !== "" && model !== "" && yearTo !== ""){
                  getSelectedCars('cars/?mark_link_text__in='+mark+'&model_link_text__in='+model+'&year__range='+year+','+yearTo)
              }
}


    const handleChangeYearTo = (year) => {
        setYearTo(year)
         if (mark !== "" && model === "" && yearFrom === ""){
             getSelectedCars('cars/?mark_link_text__in='+mark+'&year__lte='+year)
              }else if ( mark !== "" && model !== "" && yearFrom === ""){
                  getSelectedCars('cars/?mark_link_text__in='+mark+'&model_link_text__in='+model+'&year__lte='+year)
              }else if( mark !== "" && model === "" && yearFrom !== ""){
                  getSelectedCars('cars/?mark_link_text__in='+mark+'&year__range='+yearFrom+','+year)
              }else if(mark === "" && model === "" && yearFrom === ""){
                  getSelectedCars('cars/?year__lte='+ year)
              }else if( mark === "" && model === "" && yearFrom !== ""){
                  getSelectedCars('cars/?year__range=' + yearFrom + ',' + year)
              }else if( mark !== "" && model !== "" && yearFrom !== ""){
                  getSelectedCars('cars/?mark_link_text__in='+mark+'&model_link_text__in='+model+'&year__range='+yearFrom+','+year)
              }
             }

   const handlePriceFrom = (price) => {
         setPriceFrom(price)
        }

    const handlePriceTo = (price) => {
        setPriceTo(price)
        }

    const handleCurrency = (currency) => {
        setCurrency(currency)
         }

    const searchForPrice = (event) => {
        if((mark !== '' || model !== '' || yearFrom !== "" || yearTo !== "")&& currency === "USD"){
             setSelectedCars(selectedCars.filter(car => car.card_price_secondary >= priceFrom && car.card_price_secondary <= priceTo))
        }else if((mark !== '' || model !== '' || yearFrom !== "" || yearTo !== "")&& currency === "BYN"){
             setSelectedCars(selectedCars.filter(car => car.card_price_primary >= priceFrom && car.card_price_primary <= priceTo))
        }else if(mark === '' && model === '' && yearFrom === "" && yearTo === "" && currency === "BYN"){
             getSelectedCars('cars/?card_price_primary__range='+priceFrom+','+priceTo)
        }else if(mark === '' && model === '' && yearFrom === "" && yearTo === "" && currency === "USD"){
             getSelectedCars('cars/?card_price_secondary__range='+priceFrom+','+priceTo)
        }
    }

    const reset = (event) => {
        setMark('')
        setModel('')
        setYearFrom('')
        setYearTo('')
        setPriceFrom(0)
        setPriceTo(10000000)
        setCurrency('USD')
        setSelectedCars([])
        }


    if (!generalItems.length) {
        return <h3> Нет информации </h3>
    }

    return(

         <div>
          <img className="general-pic" src={general_pic} alt="fish"/>

            <GeneralLineTable/>
            <SecondAd/>
            <GeneralPageItemsTable generalItems={generalItems} cars={cars}/>
            <FindForParamsForm changedPriceFrom={handlePriceFrom} changedPriceTo={handlePriceTo}
                               changedCurrency={handleCurrency} searchForPrice={searchForPrice}
                               changedYearFrom={handleChangeYearFrom} changedYearTo={handleChangeYearTo}
                               changedModel={handleChangeModel} changedMark={handleChangeMark}
                               changedCarsCount={handleCarsCount} carsCount={carsCount} generalItems={generalItems}
                               models={models} cars={cars} reset={reset}/>

            <CarsTable carsCount={selectedCars.length} cars={selectedCars}/>
         </div>
    )
}

export default GeneralPage;


