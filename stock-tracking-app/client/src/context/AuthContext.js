import React, { createContext, useState, useEffect } from 'react';

export const AuthContext = createContext();

export const AuthProvider = ({ children }) => {
    const [user, setUser] = useState(null);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        const fetchUser = async () => {
            // Simulate fetching user data
            const response = await fetch('/api/user'); // Adjust the endpoint as needed
            const data = await response.json();
            setUser(data.user);
            setLoading(false);
        };

        fetchUser();
    }, []);

    const fetchWithAuth = async (url, method = 'GET', body = null) => {
        const token = user ? user.token : null; // Assume user object contains a token
        const headers = {
            'Content-Type': 'application/json',
            ...(token && { Authorization: `Bearer ${token}` }),
        };

        const response = await fetch(url, {
            method,
            headers,
            body: body ? JSON.stringify(body) : null,
        });

        return response.json();
    };

    return (
        <AuthContext.Provider value={{ user, loading, fetchWithAuth }}>
            {children}
        </AuthContext.Provider>
    );
};