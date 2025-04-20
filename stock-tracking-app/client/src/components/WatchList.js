import React, { useState, useEffect, useContext } from "react";
import { Card, Button, List, Input } from "antd";
import { AuthContext } from "../context/AuthContext";

const WatchList = () => {
  const { fetchWithAuth } = useContext(AuthContext);
  const [watchlist, setWatchlist] = useState([]);
  const [newStock, setNewStock] = useState("");

  useEffect(() => {
    const fetchWatchlist = async () => {
      try {
        const response = await fetchWithAuth("/api/getWatchlist", "GET");
        if (response.status) {
          setWatchlist(response.data.watchlist);
        }
      } catch (error) {
        console.error("Error fetching watchlist:", error);
      }
    };

    fetchWatchlist();
  }, [fetchWithAuth]);

  const addStock = async () => {
    if (!newStock) return;

    const stockToAdd = { label: newStock, token: newStock }; // Assuming token is the same as label for simplicity
    try {
      const response = await fetchWithAuth("/api/saveWatchlist", "POST", {
        watchlist: [...watchlist, stockToAdd],
      });
      if (response.status) {
        setWatchlist((prev) => [...prev, stockToAdd]);
        setNewStock("");
      }
    } catch (error) {
      console.error("Error adding stock:", error);
    }
  };

  const removeStock = async (token) => {
    const updatedWatchlist = watchlist.filter((stock) => stock.token !== token);
    try {
      await fetchWithAuth("/api/saveWatchlist", "POST", {
        watchlist: updatedWatchlist,
      });
      setWatchlist(updatedWatchlist);
    } catch (error) {
      console.error("Error removing stock:", error);
    }
  };

  return (
    <Card title="Watchlist">
      <Input
        value={newStock}
        onChange={(e) => setNewStock(e.target.value)}
        placeholder="Add a new stock"
        onPressEnter={addStock}
      />
      <Button onClick={addStock} type="primary" style={{ marginTop: 10 }}>
        Add Stock
      </Button>
      <List
        bordered
        dataSource={watchlist}
        renderItem={(item) => (
          <List.Item
            actions={[
              <Button type="link" onClick={() => removeStock(item.token)}>
                Remove
              </Button>,
            ]}
          >
            {item.label}
          </List.Item>
        )}
        style={{ marginTop: 10 }}
      />
    </Card>
  );
};

export default WatchList;