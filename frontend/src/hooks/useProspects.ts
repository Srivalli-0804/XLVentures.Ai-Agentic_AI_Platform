import { useEffect } from "react";

import { useProspectStore } from "../store/prospectStore";

export const useProspects = () => {
  const {
    prospects,
    contacts,
    recommendations,
    loading,
    error,
    fetchProspects,
    fetchContacts,
    fetchRecommendations,
    clearError
  } = useProspectStore();

  useEffect(() => {
    fetchProspects();
  }, []);

  return {
    prospects,
    contacts,
    recommendations,
    loading,
    error,
    fetchProspects,
    fetchContacts,
    fetchRecommendations,
    clearError
  };
};