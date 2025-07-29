// import React, { useEffect, useRef, useState } from "react";

const ContextType = "section";
const ContextId = "";
/////COMPONENET/////COMPONENET/////COMPONENET/////COMPONENET/////
/////COMPONENET/////COMPONENET/////COMPONENET/////COMPONENET/////
export default function User_infoTile({
  children,
  _className,
  _id = ContextId,
  _style,
  _user_data,
  _onClick,
  _onCompClick,
  ...rest
}: _defaultProps) {
  ///////FUNCTIONS//////////FUNCTIONS///////////FUNCTIONS///////////
  ///////FUNCTIONS//////////FUNCTIONS///////////FUNCTIONS///////////

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
      {/* {children} */}

      <div className="info_tile info_tile-title_top">
        <div className="info_tile-celd">
          <h1 className="info_tile-name">{_user_data?._name}</h1>
        </div>
      </div>

      <div className="info_tile info_tile-title_center">
        <div className="info_tile-celd">
          <h1 className="info_tile-title">Account: </h1>
          <p className="info_tile-data">{_user_data?._account}</p>
        </div>
        <div className="info_tile-celd">
          <h1 className="info_tile-title">Position: </h1>
          <p className="info_tile-data">{_user_data?._position}</p>
        </div>
      </div>
      <div className="info_tile info_tile-title_center">
        <div className="info_tile-celd info_tile-flex">
          <h1 className="info_tile-title">Wave:</h1>
          <p className="info_tile-data">{_user_data?._wave}</p>
        </div>
        <div className="info_tile-celd">
          <h1 className="info_tile-title">Status:</h1>
          <p className="info_tile-data">{_user_data?._assistance}</p>
        </div>
      </div>
      <div className="info_tile info_tile-title_end">
        <div className="info_tile-celdcenter">
          <h1 className="info_tile-title">ID:</h1>
          <p className="info_tile-data">{_user_data?._badge_ID}</p>
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
  _user_data?: _user_details;
  _onClick?: () => void;
  _onCompClick?: () => void;
};

//////////IMPORTS//////IMPORTS//////IMPORTS//////IMPORTS//////IMPORTS/////////
//////////IMPORTS//////IMPORTS//////IMPORTS//////IMPORTS//////IMPORTS/////////
//@ts-ignore
import "./User_infoTile.scss";
import { _user_details } from "../../../../models/types/userType";
