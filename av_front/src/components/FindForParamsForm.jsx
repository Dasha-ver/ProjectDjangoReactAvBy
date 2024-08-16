import React, {useState} from 'react';
import Select from "react-select";


const FindForParamsForm = ({generalItems, models, cars, defaultValue, defaultValueId, changedMark,
                            changedCarsCount, changedModel, changedYearFrom, changedYearTo,
                            changedPriceFrom, changedPriceTo, changedCurrency, searchForPrice,
                            reset}) => {

    const currency = ['USD', 'BYN']

    const currencyItems = currency.map((currencyItem) =>
        <li key={currencyItem.toString()}>
          {currencyItem}
        </li>
      );

    const [mark, setMark] = useState(defaultValue)
    const [model, setModel] = useState(null)
    const [modelList, setModelList] = useState(models.filter(t => t.mark === defaultValueId))
    const [yearFrom, setYearFrom] = useState(null)
    const [yearTo, setYearTo] = useState(null)
    const [priceFrom, setPriceFrom] = useState(null)
    const [priceTo, setPriceTo] = useState(null)
    const [selectedCurrency, setSelectedCurrency] = useState(currencyItems[0])
    const [showMore, setShowMore] = useState(true)

    const arrayRange = (start, stop, step) =>
        Array.from(
        { length: (stop - start) / step + 1 },
        (value, index) => start + index * step
        );
    var currentYear = new Date().getFullYear()

    const years = arrayRange(1910, currentYear,1).reverse()

    const yearsItems = years.map((year) =>
        <li key={year.toString()}>
          {year}
        </li>
      );



    function compare(lang, letters) {
        let cmp = new Intl.Collator(lang).compare;
        letters.sort((a, b) => (a.title > "\xff") - (b.title > "\xff") || (a.title > "\xff" ? cmp(a.title, b.title) : a.title.localeCompare(b.title))
        );
        return letters;
}


      const handleMarkChange = (obj) => {
          setModel(null)
          setYearFrom(null)
          setYearTo(null)
          setMark(obj)
          setModelList(models.filter(t => t.mark === obj.id))
          changedMark(obj.title)
          changedCarsCount(obj.count)
      }


       const handleModelChange = (obj) => {
         setModel(obj)
         setYearFrom(null)
         setYearTo(null)
         changedCarsCount(obj.count)
         changedModel(obj.title)
       }

        const handleYearFromChange = (obj) => {
          setYearFrom(obj)
          changedYearFrom(obj.key)
       }
        const handleYearToChange = (obj) => {
         setYearTo(obj)
         changedYearTo(obj.key)
       }


        const handlePriceFromChange = (e) => {
            setPriceFrom(e.target.value)
            setShowMore()
            changedPriceFrom(e.target.value)
            }


        const handleCurrency = (obj) => {
            setSelectedCurrency(obj)
            changedCurrency(obj.key)
        }

        const handleSearchForPrice =(event) => {
            searchForPrice(event)
        }

        const handlePriceToChange = (e) => {
            setShowMore()
            setPriceTo(e.target.value)
            changedPriceTo(e.target.value)
        }

        const handleReset = (event) => {
             setMark('')
            setModel('')
            setYearFrom(null)
            setYearTo(null)
            setPriceFrom("")
            setPriceTo("")
            setSelectedCurrency(currencyItems[0])
            
            reset(event)
            }


    return (
    <div>
        <div class="div-find-for-params">
        <tr>
            <td class="td-find-for-params">Поиск по параметрам</td>
            <td class='td-push-mark'><button class='btn-push-mark'>+ Марка</button></td>
        </tr>
        </div>

     <table class='table-find-for-params-first-line' >
                    <tr class='tr-find-for-params-first-line'>
                   <td class="td-find">
                        <Select
                          placeholder="Марка"
                          options={compare('zh', generalItems)}
                          value={mark}
                          onChange={handleMarkChange}
                          getOptionLabel={(generalItems) => generalItems['title']}
                          getOptionValue={(generalItems) => generalItems['id']}
                        />
                    </td>
                    <td class="td-find">
                        <Select
                          placeholder="Модель"
                          value={model}
                          options={modelList}
                          onChange={handleModelChange}
                          getOptionLabel={(modelList) => modelList['title']}
                          getOptionValue={(modelList) => modelList['id']}
                        />
                    </td>
                    </tr>
                 <tr class='tr-find-for-params-second-line'>
                     <tr class="tr-year-find-for-params-second-line">
                         <td class="td-year-params-second-line">Год</td>
                    <td class="td-find-second-year">
                        <Select
                          placeholder="От"
                          options={yearsItems}
                          value={yearFrom}
                          onChange={handleYearFromChange}
                          getOptionLabel={(yearsItems) => yearsItems['key']}
                          getOptionValue={(yearsItems) => yearsItems['key']}

                        />
                        </td>
                   <td class="td-find-second-year">
                        <Select
                          placeholder="До"
                          options={yearsItems}
                          value={yearTo}
                          onChange={handleYearToChange}
                          getOptionLabel={(yearsItems) => yearsItems['key']}
                          getOptionValue={(yearsItems) => yearsItems['key']}
                        />
                        </td>
                        </tr>

                    <td class="td-find">
                        <tr class="tr-year-find-for-params-second-line">
                         <td class="td-year-params-second-line">Цена</td>
                    <td class="td-find-second-price">
                       <input
                          onKeyPress={(event) => {
                            if (!/[0-9]/.test(event.key)) {
                              event.preventDefault();
                            }
                          }}
                          placeholder="От"
                          style={{width: "160px", height: "38px"}}
                          value={priceFrom}
                          onChange={handlePriceFromChange}

                        />
                        </td>
                   <td class="td-find-second-price">
                        <input
                          onKeyPress={(event) => {
                            if (!/[0-9]/.test(event.key)) {
                              event.preventDefault();
                            }
                          }}
                          placeholder="До"
                          style={{width: "160px", height: "38px"}}
                          value={priceTo}
                          onChange={handlePriceToChange}

                        />
                        </td>
                      <td class="td-find-currency">
                        <Select
                          options={currencyItems}
                          value={selectedCurrency}
                          onChange={handleCurrency}
                          getOptionLabel={(currencyItems) => currencyItems['key']}
                          getOptionValue={(currencyItems) => currencyItems['key']}
                        />
                        </td>
                        </tr>

                    </td>
                    </tr>
                    <tr class="tr-find-for-params-second-line">
                        <td>
                        <button onClick={handleReset} class="btn-reset">Сбросить</button>
                        </td>
                        <td class={showMore ? 'display-none' : 'display-block'}>
                         <button onClick={handleSearchForPrice} class="btn-show-ads-for-params">Искать по цене</button>
                         </td>
                        </tr>
                </table>
           </div>


)
}

export default FindForParamsForm;