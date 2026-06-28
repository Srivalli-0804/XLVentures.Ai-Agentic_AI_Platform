import { create } from "zustand";
import api from "../lib/api";
import {
  Company,
  Contact,
  Recommendation
} from "../lib/types";

interface ProspectState {
  prospects: Company[];
  contacts: Contact[];
  recommendations: Recommendation[];

  loading: boolean;
  error: string | null;

  fetchProspects: () => Promise<void>;
  fetchContacts: () => Promise<void>;
  fetchRecommendations: () => Promise<void>;

  clearError: () => void;
}

export const useProspectStore =
  create<ProspectState>((set) => ({
    prospects: [],
    contacts: [],
    recommendations: [],

    loading: false,
    error: null,

    fetchProspects: async () => {
      try {
        set({ loading: true });

        const response =
          await api.get("/prospects");

        set({
          prospects: response.data,
          loading: false
        });
      } catch (error: any) {
        set({
          loading: false,
          error:
            error?.message ||
            "Failed to load prospects"
        });
      }
    },

    fetchContacts: async () => {
      try {
        set({ loading: true });

        const response =
          await api.get("/contacts");

        set({
          contacts: response.data,
          loading: false
        });
      } catch (error: any) {
        set({
          loading: false,
          error:
            error?.message ||
            "Failed to load contacts"
        });
      }
    },

    fetchRecommendations: async () => {
      try {
        set({ loading: true });

        const response =
          await api.get(
            "/recommendations"
          );

        set({
          recommendations:
            response.data,
          loading: false
        });
      } catch (error: any) {
        set({
          loading: false,
          error:
            error?.message ||
            "Failed to load recommendations"
        });
      }
    },

    clearError: () =>
      set({
        error: null
      })
  }));