with

dim_promos as (

    select * from {{ ref('stg_greenery__promos') }}

)

select * from dim_promos
