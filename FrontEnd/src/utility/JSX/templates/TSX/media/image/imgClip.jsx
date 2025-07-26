import { useState } from "react";

export default function ImageCLip({
  HolderContainer = "img",
  className,
  _src,
  _alt = "img",
  children,
  ...props
}) {
  const [name, setName] = useState();

  return (
    <>
      <HolderContainer src={_src} alt={_alt} className={className} {...props} />
      {/* {children}
      </HolderContainer> */}
    </>
  );
}
