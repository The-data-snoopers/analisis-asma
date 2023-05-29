INSERT INTO public.year_dim (years, id_year)
VALUES ('2017', 1), ('2021', 2);


INSERT INTO public.asma_dim (asma, id_asma)
VALUES ('si', 1), ('no', 2);


SELECT * FROM public.year_dim;

SELECT * FROM public.asma_dim;

SELECT * FROM public.localidad_dim;

SELECT * FROM public.vivienda_dim;