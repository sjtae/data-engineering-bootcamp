with
fct_movements as (
    select * from {{ ref('int_movements_operating_companies__joined') }}
)

select * from fct_movements