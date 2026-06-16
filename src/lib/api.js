import axios from "axios";

// Yeh line pehle check karegi ki .env file me live Railway ka link hai ya nahi.
// Agar nahi milega, toh hi localhost:8000 par chalega.
const BACKEND_URL = import.meta.env.VITE_API_BASE_URL || "http://localhost:8000";
export const API_BASE = `${BACKEND_URL}/api`;

const api = axios.create({ baseURL: API_BASE });

api.interceptors.request.use((config) => {
  const token = localStorage.getItem("auth_token");
  if (token) config.headers.Authorization = `Bearer ${token}`;
  return config;
});

export default api;

export const formatApiError = (err) => {
  const d = err?.response?.data?.detail;
  if (!d) return err?.message || "Something went wrong";
  if (typeof d === "string") return d;
  if (Array.isArray(d)) return d.map((e) => e?.msg || JSON.stringify(e)).join(", ");
  return JSON.stringify(d);
};

export const formatPrice = (n) => `₹${Number(n).toFixed(0)}`;