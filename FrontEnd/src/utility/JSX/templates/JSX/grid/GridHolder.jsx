import "../../../sass/layout/_grid.scss";
import "../../../sass/base/_utilities.scss";
import "../../../sass/typography/_typography.scss";

import { useState } from "react";

const _row = "row";

export default function GridHolder({
  HolderContainer = "div",
  className,
  children,
  ...props
}) {
  const [name, setName] = useState();

  return (
    <>
      <HolderContainer className={`${_row} ${className}`}>
        {children}
      </HolderContainer>
    </>
  );
}
