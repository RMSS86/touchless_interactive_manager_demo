const ContextType = "div";
/////COMPONENET/////COMPONENET/////COMPONENET/////COMPONENET/////
/////COMPONENET/////COMPONENET/////COMPONENET/////COMPONENET/////
export default function TopNavigator({
  children,
  _navClassName,
  _style,
  _onClick,
  ...rest
}: _defaultProps) {
  ///////FUNCTIONS//////////FUNCTIONS///////////FUNCTIONS///////////
  ///////FUNCTIONS//////////FUNCTIONS///////////FUNCTIONS///////////
  /////USERCONTEXT////USERCONTEXT////USERCONTEXT////USERCONTEXT/////
  /////USERCONTEXT////USERCONTEXT////USERCONTEXT////USERCONTEXT/////
  //@ts-ignore
  const { globalUser, setGlobalUser } = useUserContext();
  console.log("From Top Navigator: ", globalUser);
  ////NAVIGATE////NAVIGATE////NAVIGATE////NAVIGATE////NAVIGATE////
  ////NAVIGATE////NAVIGATE////NAVIGATE////NAVIGATE////NAVIGATE////
  let _navigate = useNavigate();

  ////DIALOG////DIALOG////DIALOG////DIALOG////DIALOG////DIALOG////
  ////DIALOG////DIALOG////DIALOG////DIALOG////DIALOG////DIALOG////
  const _dialog = useRef<HTMLDialogElement>(null);

  const _invokeModal = () => {
    //@ts-ignore
    _dialog.current!.open();
  };

  const _modalCommandClose = () => {
    _dialog.current!.close();
  };
  ///////LOGOUT///////LOGOUT///////LOGOUT///////LOGOUT///////LOGOUT///////LOGOUT
  ///////LOGOUT///////LOGOUT///////LOGOUT///////LOGOUT///////LOGOUT///////LOGOUT
  /////////////////////////////////LOGOUT
  //const _logOut = useLogOut(setGlobalUser, _modalCommandClose, _navigate("/"));
  const _logOut = async () => {
    try {
      {
        /* LOGS OUT USER AND SENDS API COOKIE DELETION REQUES */
      }
      const _response: any = await FetchData({
        _endPoint: "users/logout",
        _method: "GET",
      });
      const _resData = await _response.json();
      console.log("from log out", _resData);

      if (_resData.status === "success") {
        setGlobalUser(_userDefault); //< modify to local storge
        _modalCommandClose(); //> closes de modal
        //>  DELETES STORAGE IN BROWS\ER
        //useLocalUser({ _action: "remove", _storageKey: "user" });
        //> ALERTS USER REMOVAL
        showAlert("success", "Succesflly Logged Out!");
        //> REQUESTED LOG OUT DIRECT TO HOMEPAGE
        // logActions({
        //   _action: "logout",
        //   _direct: () => _navigate("/"),
        // });
      }
    } catch (err) {
      //> ALERTS USER REMOVAL
      showAlert("success", err);
      console.log(err);
    }
  };

  function toggleSidebar() {
    const _sidebar = document.getElementById("sidebar");
    _sidebar?.classList.toggle("show");
    console.log("clicked!");
  }

  ////////RETURN/////RETURN/////RETURN/////RETURN/////RETURN/////
  ////////RETURN/////RETURN/////RETURN/////RETURN/////RETURN/////
  return (
    <>
      {/* //MODAL AREA////MODAL AREA////MODAL AREA////MODAL AREA// */}
      {/* //MODAL AREA////MODAL AREA////MODAL AREA////MODAL AREA// */}
      <SessionOutModal
        _dialog={_dialog}
        _btnCommandA={_logOut}
        _btnCommandB={_modalCommandClose}
      />
      {/* //MODAL AREA////MODAL AREA////MODAL AREA////MODAL AREA// */}
      {/* //MODAL AREA////MODAL AREA////MODAL AREA////MODAL AREA// */}

      <ContextType
        {...rest}
        className="top-nav"
        onClick={_onClick}
        style={_style}
      >
        {/* //lOGO// */}
        <HeaderSideButton _onClick={toggleSidebar} _brandingTag={BRAND_NAME} />
        {/* //SEARCH// */}
        {/* //NAV-LINKS// */}
        <TopNavLinks _userContext={globalUser} _invokeModal={_invokeModal} />
        {/* //USER AVATAR// */}
        <HeaderSideUser />
      </ContextType>
    </>
  );
}

/////TYPE/////TYPE/////TYPE/////TYPE/////TYPE/////TYPE///////
/////TYPE/////TYPE/////TYPE/////TYPE/////TYPE/////TYPE///////
type _defaultProps = {
  children?: React.ReactNode;
  _navClassName?: string;
  _style?: React.CSSProperties;

  _onClick?: () => void;
};

//////////IMPORTS//////IMPORTS//////IMPORTS//////IMPORTS///////////
//////////IMPORTS//////IMPORTS//////IMPORTS//////IMPORTS///////////
import { _menuFeatures, _userDefault } from "../../../../utility/data/data.ts";

//@ts-ignore
import "./TopNavigator.scss"; //@ts-ignore
import { useUserContext } from "../../../../store/UserContext.tsx";
import { useEffect, useRef } from "react";
import FetchData from "../../../../requests/http.ts"; //@ts-ignore
import { useNavigate } from "react-router-dom"; //@ts-ignore
import { showAlert } from "../../../../utility/imports.js";
import { logActions } from "../../../../../models/functions/userLogActions.ts";
import { useLocalUser } from "../../../../../models/hooks/useLocalUser.tsx";
//@ts-ignore
import { GeneralLogo } from "../../../../../utility/assetsImport.js";
import { useLogOut } from "../../../../../models/hooks/useLogOut.tsx";
import TopNavLinks from "./TopNavLinks.tsx";
import SessionOutModal from "../../components/cards/modal/SessionOutModal.tsx";
import HeaderSideButton from "../sections/HeaderSideButton.tsx";
import HeaderSideUser from "../sections/HeaderSideUser.tsx";
import { BRAND_NAME } from "../../../../utility/data/UI-Data/UIData.ts";
