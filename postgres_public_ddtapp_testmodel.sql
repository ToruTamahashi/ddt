create table ddtapp_testmodel
(
    id    serial       not null
        constraint ddtapp_testmodel_pkey
            primary key,
    title varchar(100) not null,
    memo  text         not null
);

alter table ddtapp_testmodel
    owner to postgres;

INSERT INTO public.ddtapp_testmodel (id, title, memo) VALUES (1, 'aaa', 'あああ');
INSERT INTO public.ddtapp_testmodel (id, title, memo) VALUES (2, 'たいとる', 'めもだお');