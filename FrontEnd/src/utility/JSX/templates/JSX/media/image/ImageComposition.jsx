import "../../../../sass/components/templates/media/image/ImageComposition_A.scss";

import { useState } from "react";

export default function ImageComposition_A({
  HolderContainer = "div",
  className,
  children,
  ...props
}) {
  const [name, setName] = useState();

  return (
    <>
      <HolderContainer className={className} {...props}>
        {children}
      </HolderContainer>
    </>
  );
}
