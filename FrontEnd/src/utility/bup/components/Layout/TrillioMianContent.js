import "./TrillioMianContent.scss";
import "../../styles/sass/_layout/Layout.scss";
import "../../styles/sass/_base/base.scss";
import Baech_dir from "../../assets/img/gallery/galleryDir";
import brandlogo from "../../assets/img/branding/Touchless_Interactive_Manager_Logo_Base_TRNSP_C.png";

import { useState, useEffect } from "react";
import _socket from "../../remoteIO/remoteIU_cmd";

import _CMD_MOUSE_MODE_ from "../../assets/pointers/TIM_Finger_Commands_AUTO-MOUSE_.png";
import _CMD_TAG_ZERO_ from "../../assets/pointers/TIM_Finger_Commands_COMMAND_ZERO_.png";
import _CMD_TAG_ONE_ from "../../assets/pointers/TIM_Finger_Commands_COMMAND_ONE_.png";
import _CMD_TAG_TWO_ from "../../assets/pointers/TIM_Finger_Commands_COMMAND_TWO_.png";
import _CMD_TAG_THREE_ from "../../assets/pointers/TIM_Finger_Commands_COMMAND_THREE_.png";
import _CMD_TAG_FOUR_ from "../../assets/pointers/TIM_Finger_Commands_COMMAND_FOUR_.png";
import _CMD_TAG_FIVE_ from "../../assets/pointers/TIM_Finger_Commands_COMMAND_FIVE_.png";

const TrillioMianContent = (props) => {
  const logoNamebase = "_CMD_TAG_";
  const [logoIndex, setLogoIndex] = useState(_CMD_TAG_FIVE_);

  useEffect(() => {
    _socket.on("userCMD_", (CMD_) => {
      //console.log(typeof message);
      //var _CMD = JSON.parse(CMD_);
      cmdSelector(CMD_);
      console.log(CMD_);
    });
  }, [_socket]);

  const cmdSelector = (_cmd) => {
    if (_cmd === "ZERO_") {
      setLogoIndex(_CMD_TAG_ZERO_);
    } else if (_cmd === "ONE_") {
      setLogoIndex(_CMD_TAG_ONE_);
    } else if (_cmd === "TWO_") {
      setLogoIndex(_CMD_TAG_TWO_);
    } else if (_cmd === "THREE_") {
      setLogoIndex(_CMD_TAG_THREE_);
    } else if (_cmd === "FOUR_") {
      setLogoIndex(_CMD_TAG_FOUR_);
    } else if (_cmd === "FIVE_") {
      setLogoIndex(_CMD_TAG_FIVE_);
    }
  };

  /*
  console.log("Logo indez value", logoIndex);
  _socket.on("userCMD_", (CMD_) => {
    //var _CMD = JSON.parse(CMD_);
    setLogoIndex(CMD_);
    console.log(CMD_);
  });
*/

  return (
    <main className="hotel-view">
      <div className="gallery">
        <figure className="gallery__item">
          <img src={brandlogo} className="brand_logo" alt="brandlogo" />
          <img
            src={_CMD_MOUSE_MODE_}
            className="command__mode"
            alt="brandlogo"
          />
          <img
            //src={_CMD_TAG_ZERO_}
            src={logoIndex}
            className="command__tag"
            alt="brandlogo"
          />
          <img
            src="http://localhost:5000/video_feed"
            alt="Web--Cam"
            className="gallery__photo"
          />
        </figure>
      </div>
    </main>
  );
};

export default TrillioMianContent;

/*
        <figure className="gallery__item">
          <img
            src={Baech_dir[1]}
            alt="Photo of hotel 1"
            className="gallery__photo"
          />
        </figure>
        <figure className="gallery__item">
          <img
            src={Baech_dir[3]}
            alt="Photo of hotel 2"
            className="gallery__photo"
          />
        </figure>
        <figure className="gallery__item">
          <img
            src={Baech_dir[4]}
            alt="Photo of hotel 3"
            className="gallery__photo"
          />
        </figure>
        */
