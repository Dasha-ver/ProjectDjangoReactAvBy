import React from 'react';
import {useNavigate} from 'react-router-dom';


const GeneralLineTable = () => {

    return(

    <table className="general-line">
                <td className="av-by">av.by</td>
                <td class="td-gen-line">
                    <div class="dropdown">
                    <button class="dropbtn">Объявления</button>
                    <div class="dropdown-content">
                    <a href="https://cars.av.by/">Автомобили с пробегом</a>
                    <a href="https://salon.av.by/">Новые автомобили</a>
                    <a href="https://cars.av.by/electrocars">Электромобили</a>
                    <a href="https://truck.av.by/">Грузовой транспорт</a>
                    <a href="https://moto.av.by/">Мототехника</a>
                    <a href="https://agro.av.by/">Сельхозтехника</a>
                    <a href="https://spec.av.by/">Спецтехника</a>
                    <a href="https://trailer.av.by/">Прицепы и полуприцепы</a>
                    <a href="https://bus.av.by/">Автобусы</a>
                    <a href="https://boat.av.by/">Водный транспорт</a>
                    <a href="https://parts.av.by/">Б/у запчасти для авто</a>
                    <a href="https://parts.av.by/accessories">Автотовары и расходники</a>
                    <a href="https://koleso.av.by/">Шины и диски</a>
                    </div>
                    </div>
                </td>
                <td class="td-gen-line">
                    <div class="dropdown">
                    <button class="dropbtn">Сервисы</button>
                    <div class="dropdown-content">
                    <a href="https://av.by/vin">Проверка VIN</a>
                    <a href="https://av.by/finance">Финансы</a>
                    <a href="https://av.by/ocenka-avto">Оценка стоимости автомобиля</a>
                    <a href="https://av.by/catalog">Каталог модификаций</a>
                    <a href="https://av.by/customs-calculator">Таможенный калькулятор</a>
                    </div>
                    </div>
                </td>
                <td class="td-gen-line">
                    <a class="dropbtn" href="https://av.by/news">Журнал</a>
                </td>
                 <td class="td-gen-line">
                    <div class="dropdown">
                    <button class="dropbtn">Знания</button>
                    <div class="dropdown-content">
                    <a href="https://av.by/pages/kak_prodat_avtomobil">Продажа автомобиля</a>
                    <a href="https://av.by/pages/kak_pravilno_pokupat_avto">Покупка автомобиля</a>
                    <a href="https://av.by/pages/buy-sell">Сделка купли-продажи</a>
                    <a href="https://av.by/pages/taxes">Налоги и сборы</a>
                    <a href="https://av.by/pages/tehosmotr">Техосмотр</a>
                    </div>
                    </div>
                </td>
                <td class="td-gen-line"><a class="dropbtn" href="https://av.by/company">Услуги</a></td>
                <td class="td-vin">
                <button class="btn-vin">
                <a class="btn-vin" href="https://av.by/vin">Проверка VIN</a></button>
                </td>
                <td class="td-enter">
                <a class="dropbtn" href="https://av.by/company">Войти</a>
                </td>
                <td class="td-place-ad">
                <button class="btn-place-ad">
                <a class="btn-place-ad" href="https://av.by/vin">Подать объявление</a></button>
                </td>
            </table>

)
}

export default GeneralLineTable;