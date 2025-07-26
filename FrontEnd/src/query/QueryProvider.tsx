import {
  QueryClientProvider,
  QueryClient,
  //QueryClientProviderProps,
} from "@tanstack/react-query";
import { ReactNode } from "react";

////CRATING A TANSTANK [PROVIDER]
const _queryClient = new QueryClient({
  defaultOptions: {
    queries: {
      refetchOnWindowFocus: false,
    },
  },
});

export const MainQueryClientProvider = ({
  children,
}: QueryClientProviderProps) => {
  return (
    <QueryClientProvider client={_queryClient}>{children}</QueryClientProvider>
  );
};

type QueryClientProviderProps = {
  children: ReactNode;
};
