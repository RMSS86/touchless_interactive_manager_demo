import { useState } from "react";

export default function ImageHolder({
  HolderContainer = "div",
  className,
  _pictureClass,
  _srcSet,
  _media,
  _imgSrcSet,
  _src,
  _alt,
  children,
  _id,
  ...props
}) {
  const [name, setName] = useState();

  return (
    <HolderContainer id={_id} className={className} {...props}>
      <picture>
        <source srcSet={_srcSet} media={_media} />
        <img
          className={_pictureClass}
          srcSet={_imgSrcSet}
          alt={_alt}
          src={_src}
        />
      </picture>
      {children}
    </HolderContainer>
  );
}
