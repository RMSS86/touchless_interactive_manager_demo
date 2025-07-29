// import React, { useEffect, useRef, useState } from "react";

const ContextType = "section";
const ContextId = "";
/////COMPONENET/////COMPONENET/////COMPONENET/////COMPONENET/////
/////COMPONENET/////COMPONENET/////COMPONENET/////COMPONENET/////
export default function User_scheduleTile({
  children,
  _className,
  _id = ContextId,
  _style,
  _onClick,
  _onCompClick,
  ...rest
}: _defaultProps) {
  ///////FUNCTIONS//////////FUNCTIONS///////////FUNCTIONS///////////
  ///////FUNCTIONS//////////FUNCTIONS///////////FUNCTIONS///////////
  const _now = new Date(Date.now()); // Get a Date object from the current timestamp

  let _options = {
    year: "numeric",
    month: "numeric",
    day: "numeric",
    hour: "numeric",
    minute: "numeric",
    second: "numeric",
    hour12: false,
    timeZone: "America/Los_Angeles",
  };

  //@ts-ignore
  const _date = new Intl.DateTimeFormat("en-US", _options).format(_now);
  ////////RETURN/////RETURN/////RETURN/////RETURN/////RETURN/////
  ////////RETURN/////RETURN/////RETURN/////RETURN/////RETURN/////
  return (
    <ContextType
      {...rest}
      id={_id}
      className={_className}
      onClick={_onClick}
      style={_style}
    >
      {children}
      <div className="schedule_tile schedule_tile-title_top">
        <div className="schedule_tile-celd">
          <h1 className="schedule_tile-name">Schedule</h1>
        </div>
      </div>

      <div className="schedule_tile schedule_tile-title_center">
        <div className="schedule_tile-celd">
          <h1 className="schedule_tile-title">Date </h1>
          <p className="schedule_tile-data">{_date.split(",")[0]}</p>
        </div>
        <div className="schedule_tile-celd">
          <h1 className="schedule_tile-title">Logged At: </h1>
          <p className="schedule_tile-data">{_date.split(",")[1]}</p>
        </div>
      </div>
      <div className="schedule_tile schedule_tile-title_center">
        <div className="schedule_tile-celd">
          <h1 className="schedule_tile-title">Aux:</h1>
          <p className="schedule_tile-data">10:45 min</p>
        </div>
        <div className="schedule_tile-celd">
          <h1 className="schedule_tile-title">Log-Total:</h1>
          <p className="schedule_tile-data">4:05 Hrs</p>
        </div>
      </div>
      <div className="schedule_tile schedule_tile-title_end">
        <div className="schedule_tile-celdcenter">
          <h1 className="schedule_tile-title">Status:</h1>
          <p className="schedule_tile-data">Lunch</p>
        </div>
      </div>
    </ContextType>
  );
}

/////TYPE/////TYPE/////TYPE/////TYPE/////TYPE/////TYPE///////
/////TYPE/////TYPE/////TYPE/////TYPE/////TYPE/////TYPE///////
type _defaultProps = {
  children?: React.ReactNode;
  _id?: string;
  _className?: string;
  _style?: React.CSSProperties;
  _onClick?: () => void;
  _onCompClick?: () => void;
};

type _dateopts = {
  day: string;
  month: string; // 'long' for full month name, 'short' for abbreviated
  year: string;
};
//////////IMPORTS//////IMPORTS//////IMPORTS//////IMPORTS//////IMPORTS/////////
//////////IMPORTS//////IMPORTS//////IMPORTS//////IMPORTS//////IMPORTS/////////
//@ts-ignore
import "./User_scheduleTile.scss";
