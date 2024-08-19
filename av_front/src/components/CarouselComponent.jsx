import React from "react";
import "react-responsive-carousel/lib/styles/carousel.min.css";
import "bootstrap/dist/css/bootstrap.min.css";
import { Carousel } from "react-responsive-carousel";

function CarouselComponent({img}) {

    const onChange = (event) => {
        console.log(event);
        };

        return (
            <div className="container">
              <Carousel infiniteLoop="true" autoPlay="true" onChange={onChange}>
                <div>
                  <img
                    className="image1"
                    src={img[0]}
                    alt="image1"
                  />
                  <p className="legend">Heading 1</p>
                </div>
                <div>
                  <img
                    className="image2"
                    src={img[0]}
                    alt="image2"
                  />
                  <p className="legend">Heading 2</p>
                </div>
                <div>
                  <img
                    className="image3"
                    src={img[2]}
                    alt="image3"
                  />
                  <p className="legend">Heading 3</p>
                </div>
              </Carousel>
            </div>
        );
        }
export default CarouselComponent;
