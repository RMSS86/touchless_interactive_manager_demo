import CardContainer from "../CardContainer_A";
import "./DoubleCard_A.scss";

import { useState } from "react";
export default function DoubleCard_A({
  _href,
  image,
  title,
  duration,
  maxNumber,
  tourGuides,
  description,
  difficulty,
  btnTag,
  logo,
  prePrice,
  price,
  HolderContainer = "div",
  className,
  children,
  _id,
  ...props
}) {
  const [name, setName] = useState();

  return (
    <>
      <HolderContainer id={_id} className={className} {...props}>
        <CardContainer className="add_another_Class_Here">
          <div className="card__side card__side-front">
            <div
              className="card__picture card__picture-1"
              style={{ backgroundImage: "url(" + image + ")" }}
            >
              {" "}
              &nbsp;
            </div>
            <h4 className="card__heading">
              <span className="card_heading-span card__heading-span-1">
                {title}
              </span>
            </h4>
            <div className="card__details">
              <ul>
                <li>{duration}</li>
                <li>{maxNumber}</li>
                <li>{tourGuides}</li>
                <li>{description}</li>
                <li>{difficulty}</li>
              </ul>
            </div>
          </div>
          <div className="card__side card__side-back card__side-back-1">
            <div className="card__cta">
              <div className="card__price-box">
                <p className="card__price-only">{prePrice}</p>
                <p className="card__price-value">{price}</p>
              </div>
              <a href={_href} className="btn btn-white">
                {btnTag}
              </a>
            </div>
          </div>
        </CardContainer>
        {children}
      </HolderContainer>
    </>
  );
}
