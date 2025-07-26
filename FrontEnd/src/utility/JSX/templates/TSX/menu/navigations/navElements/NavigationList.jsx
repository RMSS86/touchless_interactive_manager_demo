import { useState } from "react";

export default function NavList({
  HolderContainer = "nav",
  className,
  _ulClass,
  children,
  _key,
  _id,
  ...props
}) {
  const [name, setName] = useState();

  return (
    <HolderContainer id={_id} key={_key} className={className} {...props}>
      <ul className={_ulClass}>{children}</ul>
    </HolderContainer>
  );
}
