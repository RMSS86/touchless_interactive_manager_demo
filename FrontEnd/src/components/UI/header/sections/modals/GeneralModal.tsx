import { forwardRef, useImperativeHandle, useRef } from "react";
/////COMPONENET/////COMPONENET/////COMPONENET/////COMPONENET/////
/////COMPONENET/////COMPONENET/////COMPONENET/////COMPONENET/////
const GeneralModal = forwardRef(function GeneralModal(
  {
    children,
    _className = "result__modal",
    _style,
    _onClick,
    _onCommandA,
    _onCommandB,
    _message,
    ...rest
  }: _defaultProps,
  ref
) {
  ///////FUNCTIONS//////////FUNCTIONS///////////FUNCTIONS///////////
  ///////FUNCTIONS//////////FUNCTIONS///////////FUNCTIONS///////////
  const _dialog = useRef<HTMLDialogElement>(null);

  useImperativeHandle(ref, () => {
    return {
      open() {
        // _dialog.current!.showModal();
        _modalCommander();
      },
      close() {
        // _dialog.current!.showModal();
        _modalCommandClose();
      },
    };
  });

  ////////////////////////MODAL I/O
  /////////////////////////////////
  const _modalCommander = () => {
    _dialog.current!.showModal();
  };
  const _modalCommandClose = () => {
    _dialog.current?.close();
  };

  ////////RETURN/////RETURN/////RETURN/////RETURN/////RETURN/////
  ////////RETURN/////RETURN/////RETURN/////RETURN/////RETURN/////
  return createPortal(
    <motion.dialog
      ////MOTION PARAMS////MOTION PARAMS////MOTION PARAMS////
      ////MOTION PARAMS////MOTION PARAMS////MOTION PARAMS////
      variants={{
        hidden: { opacity: 0, y: 30 },
        visible: { opacity: 1, y: 0 },
      }}
      initial="hidden"
      animate="visible"
      exit="hidden"
      ////MOTION PARAMS////MOTION PARAMS////MOTION PARAMS////
      ////MOTION PARAMS////MOTION PARAMS////MOTION PARAMS////

      {...rest}
      ref={_dialog}
      className={_className}
      onClick={_onClick}
      style={_style}
    >
      {children}
    </motion.dialog>,
    document.getElementById("modal")!
  );
});

/////TYPE/////TYPE/////TYPE/////TYPE/////TYPE/////TYPE///////
/////TYPE/////TYPE/////TYPE/////TYPE/////TYPE/////TYPE///////
type _defaultProps = {
  _componentProps?: React.ComponentPropsWithRef<"dialog"> & {
    ///add alternative propierties than the native elements
  };
  _onCommandA?: () => void;
  _onCommandB?: () => void;
  _message?: string;
  children?: React.ReactNode;
  _className?: string;
  _style?: React.CSSProperties;
  _onClick?: () => void;
};

//////////IMPORTS//////IMPORTS//////IMPORTS//////IMPORTS//////IMPORTS/////////
//////////IMPORTS//////IMPORTS//////IMPORTS//////IMPORTS//////IMPORTS/////////
//@ts-ignore
import "./GeneralModal.scss";

import { AnimatePresence, motion } from "framer-motion";
import { createPortal } from "react-dom"; //@ts-ignore
// import React, { useEffect, useRef, useState } from "react";

/////EXPORTS/////EXPORTS/////EXPORTS/////EXPORTS/////EXPORTS/////EXPORTS////
/////EXPORTS/////EXPORTS/////EXPORTS/////EXPORTS/////EXPORTS/////EXPORTS////
export default GeneralModal;
{
  /* ///ENTER DEDICATED ELEMENT FOR MESSAGE FORM AND ENTER BUTTONS/// */
}
{
  /* <form method="dialog" onSubmit={_onCommandA}>
        <button>LogOut</button>
      </form>
      <button onClick={_modalCommandClose}>Cancel</button> */
}
{
  /* <ATagButton _btnText="cancel" _onClick={_modalCommandClose} /> */
}
