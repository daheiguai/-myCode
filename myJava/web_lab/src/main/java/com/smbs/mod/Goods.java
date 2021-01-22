package com.smbs.mod;

public class Goods {
    private int goodsID;
    private String goodsName;
    private int goodsPrice;
    private String goodsDiscription;
    private String userName;

    public void setGoodsDiscription(String goodsDiscription) {
        this.goodsDiscription = goodsDiscription;
    }


    public String getGoodsDiscription() {
        return goodsDiscription;
    }

    public String getUserName() {
        return userName;
    }

    public void setUserName(String userName) {
        this.userName = userName;
    }

    public int getGoodsID() {
        return goodsID;
    }

    public void setGoodsID(int goodsID) {
        this.goodsID = goodsID;
    }

    public String getGoodsName() {
        return goodsName;
    }

    public void setGoodsName(String goodsName) {
        this.goodsName = goodsName;
    }

    public int getGoodsPrice() {
        return goodsPrice;
    }

    public void setGoodsPrice(int goodsPrice) {
        this.goodsPrice = goodsPrice;
    }

}
