import { Fragment } from "react";
import ReactDOM from "react-dom";
import "./Modal.scss";

const Backdrop = (props) => {
  return <div className="backdrop" onClick={props.onClose}></div>;
};

const ModalOverlay = (props) => {
  return (
    <div className="modal">
      <div className="content">{props.children}</div>;
    </div>
  );
};

const portElm = document.getElementById("overlays");

const Modal = (props) => {
  return (
    <Fragment>
      {ReactDOM.createPortal(<Backdrop onClose={props.onClose} />, portElm)}
      {ReactDOM.createPortal(
        <ModalOverlay>{props.children}</ModalOverlay>,
        portElm
      )}
    </Fragment>
  );
}; //with portals on ReactDOM

export default Modal;
