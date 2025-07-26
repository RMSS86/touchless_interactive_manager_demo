import "../../../../sass/components/templates/cards/bullets/InfoBullet.scss";

import { useState } from "react";

export default function InfoBullet({
  HolderContainer = "div",
  className,
  _id,
  children,
  ...props
}) {
  const [name, setName] = useState();

  return (
    <>
      <HolderContainer id={_id} className={className} {...props}>
        {children}
      </HolderContainer>
    </>
  );
}
