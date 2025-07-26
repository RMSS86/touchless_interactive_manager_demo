import { Fragment } from "react";
import "./BG-Video.scss";
import MealRawVideo from "../../assets/videos/raw/21Bites_Logo_BG-Vid-A.mp4";
///import MealRawVideo from "../../assets/videos/raw/21GMRS_Header_One.mp4";

const BGVideo = () => {
  return (
    <Fragment className="bg-video">
      <video
        className="bg-video__content"
        src={MealRawVideo}
        type="video/mp4"
        autoPlay
        muted
        loop
      >
        {/* <source  /> */}
        {/* <source src="img/video.webm" type="video/webm" /> */}
        Your browser is not supported!
      </video>
    </Fragment>
  );
};

export default BGVideo;
