create database HotelManagementSystems;
use HotelManagementSystems;
create table Customers(
Cust_ID int,
Cust_Name varchar(20),
Cust_City varchar(20),
Cust_RoomNo int,
CheckIn_Time datetime,
)
select * from Customers;
insert into Customers(Cust_ID,Cust_Name,Cust_City,Cust_RoomNo,CheckIn_Time)
values('001','PRIYANKA','Maryland','201','2023-3-3 11:00' ),('002','ADITI','Newyork','304','2023-4-6 13:00'),('003','NEHA','Delaware','705','2023-1-9 15:00'),('004','RIDHI','LA','320','2023-9-2 12:00'),('005','AKASH','PA','212','2023-1-1');