import { useState } from "react";

export default function SectionHolder({
  HolderContainer = "section",
  _id,
  className,
  children,
  ...props
}) {
  const [name, setName] = useState();

  return (
    <>
      <HolderContainer className={className} {...props} id={_id}>
        {children}
      </HolderContainer>
    </>
  );
}
