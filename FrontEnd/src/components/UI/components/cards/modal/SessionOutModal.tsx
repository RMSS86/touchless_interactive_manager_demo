// import React, { useEffect, useRef, useState } from "react";

import TagButton from "../../buttons/TagButton";
import ModalCardStandard from "./ModalCard";

const ContextId = "";
/////COMPONENET/////COMPONENET/////COMPONENET/////COMPONENET/////
/////COMPONENET/////COMPONENET/////COMPONENET/////COMPONENET/////
export default function SessionOutModal({
  children,
  _className,
  _id = ContextId,
  _style,
  _dialog,
  _onClick,
  _btnCommandA,
  _btnCommandB,
  _btnCommandC,
  _onCompClick,
  ...rest
}: _defaultProps) {
  ///////FUNCTIONS//////////FUNCTIONS///////////FUNCTIONS///////////
  ///////FUNCTIONS//////////FUNCTIONS///////////FUNCTIONS///////////

  ////////RETURN/////RETURN/////RETURN/////RETURN/////RETURN/////
  ////////RETURN/////RETURN/////RETURN/////RETURN/////RETURN/////
  return (
    <>
      <GeneralModal ref={_dialog}>
        <ModalCardStandard
          _brandingBGSrc={GeneralLogo}
          _brandinglogosrc={GeneralLogo}
          _msgTag="Are you Sure to Log Out?"
          _imgSrc={GeneralLogo}
        >
          <TagButton
            _btnText="LogOut"
            _onClick={_btnCommandA}
            _className="btn btn--green"
          />
          <TagButton
            _btnText="Cancel"
            _onClick={_btnCommandB}
            _className="btn btn--white"
          />
        </ModalCardStandard>
      </GeneralModal>
      {/* //MODAL AREA////MODAL AREA////MODAL AREA////MODAL AREA// */}
      {/* //MODAL AREA////MODAL AREA////MODAL AREA////MODAL AREA// */}
    </>
  );
}

/////TYPE/////TYPE/////TYPE/////TYPE/////TYPE/////TYPE///////
/////TYPE/////TYPE/////TYPE/////TYPE/////TYPE/////TYPE///////
type _defaultProps = {
  children?: React.ReactNode;
  _id?: string;
  _dialog: React.Ref<unknown> | undefined;
  _className?: string;
  _style?: React.CSSProperties;
  _btnCommandA?: () => void; //Promise<void>;
  _btnCommandB?: () => void;
  _btnCommandC?: () => void;
  _onClick?: () => void;
  _onCompClick?: () => void;
};

//////////IMPORTS//////IMPORTS//////IMPORTS//////IMPORTS//////IMPORTS/////////
//////////IMPORTS//////IMPORTS//////IMPORTS//////IMPORTS//////IMPORTS/////////
//@ts-ignore
import { GeneralLogo } from "../../../../../utility/assetsImport.js";
import GeneralModal from "../../modals/GeneralModal.js";
