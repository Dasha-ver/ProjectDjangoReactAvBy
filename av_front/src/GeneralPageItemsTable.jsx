import React, {useState} from 'react';
import GeneralItem from "./GeneralItem";


const GeneralPageItemsTable = ({generalItems, cars}) => {

     const [showMore, setShowMore] = useState(false)

        return(

        <div>

             <table>
                    <tr class="tr-advertisment-fish">
                    <td class="td-number-of-advertisment"><div> {cars.length} объявлений <br/> о продаже авто в Беларуси </div>
                    </td>
                    <td class='td-btn-fish'>
                    <a href="https://www.youtube.com/watch?v=LIjbN9yN8_w">
                        <button class="btn-fish"></button>
                        </a>
                    </td>
                    </tr>
                    </table>
               <table class="general-page-items-table">
                    {showMore
                    ? generalItems.map(generalItem => <GeneralItem generalItem={generalItem} key={generalItem.id}/>)
                    : generalItems.slice(0,30).map(generalItem => <GeneralItem generalItem={generalItem} key={generalItem.id}/>)
                    }
                 </table>
                <div class={showMore ? 'display-none' : 'display-block'}>
                 <button class="btn-show-more" onClick= {() => setShowMore((s) => !s)}>Все марки</button>
                </div>
          </div>


)
}
export default GeneralPageItemsTable;