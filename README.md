# Project Name
Farkito api

## Table of Contents
* [Features](#features)
* [Setup](#setup)
* [Usage](#usage)
* [Acknowledgements](#acknowledgements)

# Features
## Filters
- Filter feature for restaurent 
- Filter feature for order
- Filter feature for food
- Filter feature for geolocation
## KPI
- KPI information

## Payment
- Payment information

## Favourite restaurent and meal
- favourite meals and restaurents for every customer

## Reset Password
- every customer or restaurent owner can change their password using mail




## Update restaurent-owner



# Setup
$ docker-compose build --no-cache

$ docker-compose run app sh -c "python manage.py makemigrations"

$ docker-compose run app sh -c "python manage.py migrate"

$ docker-compose run app sh -c "python manage.py populate_restaurent"


# Usage

## Filters

## API introduction
This application use Django framework with django-filter package.

## Routes about Filter
### restaurent filter
GET | /api/restaurent/restaurents/

Params : 
* name: string
* name__contains:string
* categories__name:string
* categories__name__contains=string
* uuid:string
* is_active:boolean
* is_open:boolean
* have_delivery:boolean
* have_takeaway:boolean
* have_onsite:boolean
* accept_cash:boolean
* accept_card:boolean
* owner:int
* created_at__gt:date
* created_at__lt:date
* table_number__gt:int
* table_number__lt:int
* capacity__gt:int
* capacity__lt:int
* telephone:string
* reviews__rating__gt:float
* reviews__rating__lt:float

Id:nothing

return: json response with status 200

remarks: gt and lt means greater than and lesser than  

Exemple of URL: /api/restaurent/restaurents/?name=Pottier+S.A.R.L.&categories__name=Mexican&uuid=0faceb42-43e7-4343-b3c5-cdfb994f43d7&is_active=true&is_open=true&have_delivery=false&have_takeaway=false&have_onsite=false&accept_cash=true&accept_card=true&owner=&created_at__gt=2022-09-26T13%3A01%3A38.687096Z&created_at__lt=2022-09-28T13%3A01%3A38.687096Z&table_number__gt=20&table_number__lt=26&capacity__gt=30&capacity__lt=67&telephone=0381818145&reviews__rating__gt=2.0&reviews__rating__lt=4/restaurent/restaurents/?name=Pottier+S.A.R.L.&categories__name=Mexican&uuid=0faceb42-43e7-4343-b3c5-cdfb994f43d7&is_active=true&is_open=true&have_delivery=false&have_takeaway=false&have_onsite=false&accept_cash=true&accept_card=true&owner=&created_at__gt=2022-09-26T13%3A01%3A38.687096Z&created_at__lt=2022-09-28T13%3A01%3A38.687096Z&table_number__gt=20&table_number__lt=26&capacity__gt=30&capacity__lt=67&telephone=0381818145&reviews__rating__gt=2.0&reviews__rating__lt=4

### order filter
GET | /api/order/orders/

Params : 
* uuid:string
* restaurent__uuid: string
* customer:int
* status:boolean
* billing_status:boolean
* total_paid:int
* order_key:string
* order_key__contains:string
* created_at__gt:date
* created_at__lt:date
* phone_number:string
* date_time__gt:date
* date_time__lt:date


Id:nothing

return: json response with status 200

remarks: gt and lt means greater than and lesser than  

Exemple of URL: /api/order/orders/?restaurent__uuid=7adb66ac-5b03-47c1-9111-00d710fcfe5a&uuid=6ed87f1f-b9dc-45b1-93d4-f99f12e6471c&customer=9&phone_number=%2B21658741196&created_at__gt=2022-10-18T07%3A29%3A51.302791Z&created_at__lt=2022-10-20T07%3A29%3A51.302791Z&total_paid=35&service=&order_key=POSDSDERWE&billing_status=&status=&date_time__gt=&date_time__lt=


### meal filter
GET | /api/food/meal/

Params : 
* name:string
* categories__name: string
* categories__name__contains:string
* rating__gt:int
* rating__lt:int
* regular_price__gt:int
* regular_price__lt:int
* discount__gt:int
* discount__lt:int
* created_at__lt:date
* created_at__gt:date
* is_available:boolean
* ingredients__name:string
* ingredients__name__contains:string
* restaurent__uuid:string
* is_active

Id:nothing

return: json response with status 200

remarks: gt and lt means greater than and lesser than  

Exemple of URL: /api/food/meal/?categories__name=Fish&name=Caesar+Salad&rating__gt=1&rating__lt=4&regular_price__gt=20&regular_price__lt=30&discount__gt=11&discount__lt=40&is_available=true&ingredients__name=Salmon&restaurent__uuid=7a738b62-d59b-430c-b598-1812bcd01578&is_active=true

### geolocation filter
GET | /api/restaurent/restaurents/

Params : 
* latitude:float
* longitude:float
* radius:float

Id:nothing

return: json response with status 200

Exemple of URL: /api/restaurent/restaurents/?latitude=36.1678&longitude=10.1765&radius=1.0

## Update restaurent-owner
put| /api/user/update-owner/identifier/
Id:nothing
params:nothing


## KPI
GET | /api/order/kpi/

Params : nothing 

Id:nothing

return: json response with status 200


## Payment
- POST | /api/payments/

Params : nothing 

Id:nothing

return: json response with status 200 with json reponse of payment-url and payment-ref

- GET | /api/payments/

Params : 

- payment_ref:slug

Id:nothing


return: json response with status 200 and information about the payment

- GET | /api/payments/orders

Params : nothing 

Id:nothing

return: json response with status 200 with all the payment orders


## Favourite restaurent and meal

- GET | /api/restaurent/restaurents/favourites/

Params : nothing 

Id:nothing

return: json response with status 200


- GET | /api/food/meal/favourites/

Params : nothing 

Id:nothing

return: json response with status 200



## Reset password

- POST | /api/rest-auth/password/reset/

Params : nothing 

Id:nothing

body:
- email

return: json response with status 200 with json reponse "the email has been sent"


## restaurent-with-meals
-Render same restaurent page with meals


# Usage

Exemple of URL: /api/restaurent/restaurents/?latitude=36.1678&longitude=10.1765&radius=1.0

## restaurent-with-meals
GET |  /api/restaurent/restaurents-meals/
 
remark:you can use filter on it