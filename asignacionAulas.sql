PGDMP       3    
            |            asignacion_a    17.1    17.1 E    
           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                           false                       0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                           false                       0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                           false                       1262    16756    asignacion_a    DATABASE     �   CREATE DATABASE asignacion_a WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'Spanish_Colombia.1252';
    DROP DATABASE asignacion_a;
                     postgres    false            �            1259    16808    agenda    TABLE     3  CREATE TABLE public.agenda (
    id_agenda integer NOT NULL,
    fecha date NOT NULL,
    hora_inicio time without time zone NOT NULL,
    hora_fin time without time zone NOT NULL,
    num_aula integer NOT NULL,
    id_grupo integer NOT NULL,
    CONSTRAINT agenda_check CHECK ((hora_fin > hora_inicio))
);
    DROP TABLE public.agenda;
       public         heap r       postgres    false            �            1259    16807    agenda_id_agenda_seq    SEQUENCE     �   CREATE SEQUENCE public.agenda_id_agenda_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 +   DROP SEQUENCE public.agenda_id_agenda_seq;
       public               postgres    false    228                       0    0    agenda_id_agenda_seq    SEQUENCE OWNED BY     M   ALTER SEQUENCE public.agenda_id_agenda_seq OWNED BY public.agenda.id_agenda;
          public               postgres    false    227            �            1259    16820    agenda_profesor    TABLE     �   CREATE TABLE public.agenda_profesor (
    id_agenda integer NOT NULL,
    id_profesor integer NOT NULL,
    disponibilidad boolean NOT NULL
);
 #   DROP TABLE public.agenda_profesor;
       public         heap r       postgres    false            �            1259    16758    aula    TABLE     �  CREATE TABLE public.aula (
    num_aula integer NOT NULL,
    capacidad integer NOT NULL,
    piso_aula integer NOT NULL,
    estado_aula character varying(50) NOT NULL,
    CONSTRAINT aula_capacidad_check CHECK ((capacidad > 0)),
    CONSTRAINT aula_estado_aula_check CHECK (((estado_aula)::text = ANY ((ARRAY['Disponible'::character varying, 'Ocupada'::character varying, 'Mantenimiento'::character varying])::text[])))
);
    DROP TABLE public.aula;
       public         heap r       postgres    false            �            1259    16757    aula_num_aula_seq    SEQUENCE     �   CREATE SEQUENCE public.aula_num_aula_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 (   DROP SEQUENCE public.aula_num_aula_seq;
       public               postgres    false    218                       0    0    aula_num_aula_seq    SEQUENCE OWNED BY     G   ALTER SEQUENCE public.aula_num_aula_seq OWNED BY public.aula.num_aula;
          public               postgres    false    217            �            1259    16783    curso    TABLE     c  CREATE TABLE public.curso (
    id_curso integer NOT NULL,
    nombre_curso character varying(100) NOT NULL,
    grupo_curso character varying(50) NOT NULL,
    jornada character varying(50) NOT NULL,
    cupoestudiantes integer NOT NULL,
    profesor_asignado integer NOT NULL,
    CONSTRAINT curso_cupoestudiantes_check CHECK ((cupoestudiantes > 0))
);
    DROP TABLE public.curso;
       public         heap r       postgres    false            �            1259    16850    curso_horario    TABLE     �   CREATE TABLE public.curso_horario (
    id_horario integer NOT NULL,
    id_curso integer NOT NULL,
    sesion character varying(50) NOT NULL
);
 !   DROP TABLE public.curso_horario;
       public         heap r       postgres    false            �            1259    16782    curso_id_curso_seq    SEQUENCE     �   CREATE SEQUENCE public.curso_id_curso_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 )   DROP SEQUENCE public.curso_id_curso_seq;
       public               postgres    false    224                       0    0    curso_id_curso_seq    SEQUENCE OWNED BY     I   ALTER SEQUENCE public.curso_id_curso_seq OWNED BY public.curso.id_curso;
          public               postgres    false    223            �            1259    16796 
   estudiante    TABLE     (  CREATE TABLE public.estudiante (
    cod_estudiante integer NOT NULL,
    dni_estudiante character varying(15) NOT NULL,
    primer_nombre character varying(50) NOT NULL,
    segundo_nombre character varying(50),
    primer_apellido character varying(50) NOT NULL,
    segundo_apellido character varying(50),
    semestre_cursante integer NOT NULL,
    direccion character varying(200),
    e_mail character varying(100) NOT NULL,
    telefono character varying(15),
    CONSTRAINT estudiante_semestre_cursante_check CHECK ((semestre_cursante > 0))
);
    DROP TABLE public.estudiante;
       public         heap r       postgres    false            �            1259    16795    estudiante_cod_estudiante_seq    SEQUENCE     �   CREATE SEQUENCE public.estudiante_cod_estudiante_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 4   DROP SEQUENCE public.estudiante_cod_estudiante_seq;
       public               postgres    false    226                       0    0    estudiante_cod_estudiante_seq    SEQUENCE OWNED BY     _   ALTER SEQUENCE public.estudiante_cod_estudiante_seq OWNED BY public.estudiante.cod_estudiante;
          public               postgres    false    225            �            1259    16865    estudiante_curso    TABLE     �   CREATE TABLE public.estudiante_curso (
    id_estudiante integer NOT NULL,
    id_curso integer NOT NULL,
    estado character varying(50) NOT NULL,
    modalidad character varying(50) NOT NULL
);
 $   DROP TABLE public.estudiante_curso;
       public         heap r       postgres    false            �            1259    16774    horario    TABLE       CREATE TABLE public.horario (
    id_horario integer NOT NULL,
    dia_semana character varying(15) NOT NULL,
    hora_inicio time without time zone NOT NULL,
    hora_fin time without time zone NOT NULL,
    CONSTRAINT horario_check CHECK ((hora_fin > hora_inicio)),
    CONSTRAINT horario_dia_semana_check CHECK (((dia_semana)::text = ANY ((ARRAY['Lunes'::character varying, 'Martes'::character varying, 'Miércoles'::character varying, 'Jueves'::character varying, 'Viernes'::character varying])::text[])))
);
    DROP TABLE public.horario;
       public         heap r       postgres    false            �            1259    16773    horario_id_horario_seq    SEQUENCE     �   CREATE SEQUENCE public.horario_id_horario_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 -   DROP SEQUENCE public.horario_id_horario_seq;
       public               postgres    false    222                       0    0    horario_id_horario_seq    SEQUENCE OWNED BY     Q   ALTER SEQUENCE public.horario_id_horario_seq OWNED BY public.horario.id_horario;
          public               postgres    false    221            �            1259    16767    profesor    TABLE     .  CREATE TABLE public.profesor (
    id_profesor integer NOT NULL,
    primer_nombre character varying(50) NOT NULL,
    segundo_nombre character varying(50),
    primer_apellido character varying(50) NOT NULL,
    segundo_apellido character varying(50),
    profesion character varying(100) NOT NULL
);
    DROP TABLE public.profesor;
       public         heap r       postgres    false            �            1259    16835    profesor_horario    TABLE     �   CREATE TABLE public.profesor_horario (
    id_profesor integer NOT NULL,
    id_horario integer NOT NULL,
    jornada character varying(50) NOT NULL
);
 $   DROP TABLE public.profesor_horario;
       public         heap r       postgres    false            �            1259    16766    profesor_id_profesor_seq    SEQUENCE     �   CREATE SEQUENCE public.profesor_id_profesor_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 /   DROP SEQUENCE public.profesor_id_profesor_seq;
       public               postgres    false    220                       0    0    profesor_id_profesor_seq    SEQUENCE OWNED BY     U   ALTER SEQUENCE public.profesor_id_profesor_seq OWNED BY public.profesor.id_profesor;
          public               postgres    false    219            ?           2604    16811    agenda id_agenda    DEFAULT     t   ALTER TABLE ONLY public.agenda ALTER COLUMN id_agenda SET DEFAULT nextval('public.agenda_id_agenda_seq'::regclass);
 ?   ALTER TABLE public.agenda ALTER COLUMN id_agenda DROP DEFAULT;
       public               postgres    false    227    228    228            :           2604    16761    aula num_aula    DEFAULT     n   ALTER TABLE ONLY public.aula ALTER COLUMN num_aula SET DEFAULT nextval('public.aula_num_aula_seq'::regclass);
 <   ALTER TABLE public.aula ALTER COLUMN num_aula DROP DEFAULT;
       public               postgres    false    218    217    218            =           2604    16786    curso id_curso    DEFAULT     p   ALTER TABLE ONLY public.curso ALTER COLUMN id_curso SET DEFAULT nextval('public.curso_id_curso_seq'::regclass);
 =   ALTER TABLE public.curso ALTER COLUMN id_curso DROP DEFAULT;
       public               postgres    false    223    224    224            >           2604    16799    estudiante cod_estudiante    DEFAULT     �   ALTER TABLE ONLY public.estudiante ALTER COLUMN cod_estudiante SET DEFAULT nextval('public.estudiante_cod_estudiante_seq'::regclass);
 H   ALTER TABLE public.estudiante ALTER COLUMN cod_estudiante DROP DEFAULT;
       public               postgres    false    226    225    226            <           2604    16777    horario id_horario    DEFAULT     x   ALTER TABLE ONLY public.horario ALTER COLUMN id_horario SET DEFAULT nextval('public.horario_id_horario_seq'::regclass);
 A   ALTER TABLE public.horario ALTER COLUMN id_horario DROP DEFAULT;
       public               postgres    false    222    221    222            ;           2604    16770    profesor id_profesor    DEFAULT     |   ALTER TABLE ONLY public.profesor ALTER COLUMN id_profesor SET DEFAULT nextval('public.profesor_id_profesor_seq'::regclass);
 C   ALTER TABLE public.profesor ALTER COLUMN id_profesor DROP DEFAULT;
       public               postgres    false    219    220    220                      0    16808    agenda 
   TABLE DATA           ]   COPY public.agenda (id_agenda, fecha, hora_inicio, hora_fin, num_aula, id_grupo) FROM stdin;
    public               postgres    false    228   �Z                 0    16820    agenda_profesor 
   TABLE DATA           Q   COPY public.agenda_profesor (id_agenda, id_profesor, disponibilidad) FROM stdin;
    public               postgres    false    229   [       �          0    16758    aula 
   TABLE DATA           K   COPY public.aula (num_aula, capacidad, piso_aula, estado_aula) FROM stdin;
    public               postgres    false    218   3[       �          0    16783    curso 
   TABLE DATA           q   COPY public.curso (id_curso, nombre_curso, grupo_curso, jornada, cupoestudiantes, profesor_asignado) FROM stdin;
    public               postgres    false    224   P[                 0    16850    curso_horario 
   TABLE DATA           E   COPY public.curso_horario (id_horario, id_curso, sesion) FROM stdin;
    public               postgres    false    231   m[                 0    16796 
   estudiante 
   TABLE DATA           �   COPY public.estudiante (cod_estudiante, dni_estudiante, primer_nombre, segundo_nombre, primer_apellido, segundo_apellido, semestre_cursante, direccion, e_mail, telefono) FROM stdin;
    public               postgres    false    226   �[                 0    16865    estudiante_curso 
   TABLE DATA           V   COPY public.estudiante_curso (id_estudiante, id_curso, estado, modalidad) FROM stdin;
    public               postgres    false    232   �[       �          0    16774    horario 
   TABLE DATA           P   COPY public.horario (id_horario, dia_semana, hora_inicio, hora_fin) FROM stdin;
    public               postgres    false    222   �[       �          0    16767    profesor 
   TABLE DATA           |   COPY public.profesor (id_profesor, primer_nombre, segundo_nombre, primer_apellido, segundo_apellido, profesion) FROM stdin;
    public               postgres    false    220   �[                 0    16835    profesor_horario 
   TABLE DATA           L   COPY public.profesor_horario (id_profesor, id_horario, jornada) FROM stdin;
    public               postgres    false    230   �[                  0    0    agenda_id_agenda_seq    SEQUENCE SET     C   SELECT pg_catalog.setval('public.agenda_id_agenda_seq', 1, false);
          public               postgres    false    227                       0    0    aula_num_aula_seq    SEQUENCE SET     @   SELECT pg_catalog.setval('public.aula_num_aula_seq', 1, false);
          public               postgres    false    217                       0    0    curso_id_curso_seq    SEQUENCE SET     A   SELECT pg_catalog.setval('public.curso_id_curso_seq', 1, false);
          public               postgres    false    223                       0    0    estudiante_cod_estudiante_seq    SEQUENCE SET     L   SELECT pg_catalog.setval('public.estudiante_cod_estudiante_seq', 1, false);
          public               postgres    false    225                       0    0    horario_id_horario_seq    SEQUENCE SET     E   SELECT pg_catalog.setval('public.horario_id_horario_seq', 1, false);
          public               postgres    false    221                       0    0    profesor_id_profesor_seq    SEQUENCE SET     G   SELECT pg_catalog.setval('public.profesor_id_profesor_seq', 1, false);
          public               postgres    false    219            T           2606    16814    agenda agenda_pkey 
   CONSTRAINT     W   ALTER TABLE ONLY public.agenda
    ADD CONSTRAINT agenda_pkey PRIMARY KEY (id_agenda);
 <   ALTER TABLE ONLY public.agenda DROP CONSTRAINT agenda_pkey;
       public                 postgres    false    228            V           2606    16824 $   agenda_profesor agenda_profesor_pkey 
   CONSTRAINT     v   ALTER TABLE ONLY public.agenda_profesor
    ADD CONSTRAINT agenda_profesor_pkey PRIMARY KEY (id_agenda, id_profesor);
 N   ALTER TABLE ONLY public.agenda_profesor DROP CONSTRAINT agenda_profesor_pkey;
       public                 postgres    false    229    229            H           2606    16765    aula aula_pkey 
   CONSTRAINT     R   ALTER TABLE ONLY public.aula
    ADD CONSTRAINT aula_pkey PRIMARY KEY (num_aula);
 8   ALTER TABLE ONLY public.aula DROP CONSTRAINT aula_pkey;
       public                 postgres    false    218            Z           2606    16854     curso_horario curso_horario_pkey 
   CONSTRAINT     p   ALTER TABLE ONLY public.curso_horario
    ADD CONSTRAINT curso_horario_pkey PRIMARY KEY (id_horario, id_curso);
 J   ALTER TABLE ONLY public.curso_horario DROP CONSTRAINT curso_horario_pkey;
       public                 postgres    false    231    231            N           2606    16789    curso curso_pkey 
   CONSTRAINT     T   ALTER TABLE ONLY public.curso
    ADD CONSTRAINT curso_pkey PRIMARY KEY (id_curso);
 :   ALTER TABLE ONLY public.curso DROP CONSTRAINT curso_pkey;
       public                 postgres    false    224            \           2606    16869 &   estudiante_curso estudiante_curso_pkey 
   CONSTRAINT     y   ALTER TABLE ONLY public.estudiante_curso
    ADD CONSTRAINT estudiante_curso_pkey PRIMARY KEY (id_estudiante, id_curso);
 P   ALTER TABLE ONLY public.estudiante_curso DROP CONSTRAINT estudiante_curso_pkey;
       public                 postgres    false    232    232            P           2606    16806 (   estudiante estudiante_dni_estudiante_key 
   CONSTRAINT     m   ALTER TABLE ONLY public.estudiante
    ADD CONSTRAINT estudiante_dni_estudiante_key UNIQUE (dni_estudiante);
 R   ALTER TABLE ONLY public.estudiante DROP CONSTRAINT estudiante_dni_estudiante_key;
       public                 postgres    false    226            R           2606    16804    estudiante estudiante_pkey 
   CONSTRAINT     d   ALTER TABLE ONLY public.estudiante
    ADD CONSTRAINT estudiante_pkey PRIMARY KEY (cod_estudiante);
 D   ALTER TABLE ONLY public.estudiante DROP CONSTRAINT estudiante_pkey;
       public                 postgres    false    226            L           2606    16781    horario horario_pkey 
   CONSTRAINT     Z   ALTER TABLE ONLY public.horario
    ADD CONSTRAINT horario_pkey PRIMARY KEY (id_horario);
 >   ALTER TABLE ONLY public.horario DROP CONSTRAINT horario_pkey;
       public                 postgres    false    222            X           2606    16839 &   profesor_horario profesor_horario_pkey 
   CONSTRAINT     y   ALTER TABLE ONLY public.profesor_horario
    ADD CONSTRAINT profesor_horario_pkey PRIMARY KEY (id_profesor, id_horario);
 P   ALTER TABLE ONLY public.profesor_horario DROP CONSTRAINT profesor_horario_pkey;
       public                 postgres    false    230    230            J           2606    16772    profesor profesor_pkey 
   CONSTRAINT     ]   ALTER TABLE ONLY public.profesor
    ADD CONSTRAINT profesor_pkey PRIMARY KEY (id_profesor);
 @   ALTER TABLE ONLY public.profesor DROP CONSTRAINT profesor_pkey;
       public                 postgres    false    220            ^           2606    16815    agenda agenda_num_aula_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.agenda
    ADD CONSTRAINT agenda_num_aula_fkey FOREIGN KEY (num_aula) REFERENCES public.aula(num_aula);
 E   ALTER TABLE ONLY public.agenda DROP CONSTRAINT agenda_num_aula_fkey;
       public               postgres    false    228    4680    218            _           2606    16825 .   agenda_profesor agenda_profesor_id_agenda_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.agenda_profesor
    ADD CONSTRAINT agenda_profesor_id_agenda_fkey FOREIGN KEY (id_agenda) REFERENCES public.agenda(id_agenda);
 X   ALTER TABLE ONLY public.agenda_profesor DROP CONSTRAINT agenda_profesor_id_agenda_fkey;
       public               postgres    false    4692    229    228            `           2606    16830 0   agenda_profesor agenda_profesor_id_profesor_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.agenda_profesor
    ADD CONSTRAINT agenda_profesor_id_profesor_fkey FOREIGN KEY (id_profesor) REFERENCES public.profesor(id_profesor);
 Z   ALTER TABLE ONLY public.agenda_profesor DROP CONSTRAINT agenda_profesor_id_profesor_fkey;
       public               postgres    false    4682    229    220            c           2606    16860 )   curso_horario curso_horario_id_curso_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.curso_horario
    ADD CONSTRAINT curso_horario_id_curso_fkey FOREIGN KEY (id_curso) REFERENCES public.curso(id_curso);
 S   ALTER TABLE ONLY public.curso_horario DROP CONSTRAINT curso_horario_id_curso_fkey;
       public               postgres    false    231    224    4686            d           2606    16855 +   curso_horario curso_horario_id_horario_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.curso_horario
    ADD CONSTRAINT curso_horario_id_horario_fkey FOREIGN KEY (id_horario) REFERENCES public.horario(id_horario);
 U   ALTER TABLE ONLY public.curso_horario DROP CONSTRAINT curso_horario_id_horario_fkey;
       public               postgres    false    4684    222    231            ]           2606    16790 "   curso curso_profesor_asignado_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.curso
    ADD CONSTRAINT curso_profesor_asignado_fkey FOREIGN KEY (profesor_asignado) REFERENCES public.profesor(id_profesor);
 L   ALTER TABLE ONLY public.curso DROP CONSTRAINT curso_profesor_asignado_fkey;
       public               postgres    false    4682    224    220            e           2606    16875 /   estudiante_curso estudiante_curso_id_curso_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.estudiante_curso
    ADD CONSTRAINT estudiante_curso_id_curso_fkey FOREIGN KEY (id_curso) REFERENCES public.curso(id_curso);
 Y   ALTER TABLE ONLY public.estudiante_curso DROP CONSTRAINT estudiante_curso_id_curso_fkey;
       public               postgres    false    224    232    4686            f           2606    16870 4   estudiante_curso estudiante_curso_id_estudiante_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.estudiante_curso
    ADD CONSTRAINT estudiante_curso_id_estudiante_fkey FOREIGN KEY (id_estudiante) REFERENCES public.estudiante(cod_estudiante);
 ^   ALTER TABLE ONLY public.estudiante_curso DROP CONSTRAINT estudiante_curso_id_estudiante_fkey;
       public               postgres    false    226    232    4690            a           2606    16845 1   profesor_horario profesor_horario_id_horario_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.profesor_horario
    ADD CONSTRAINT profesor_horario_id_horario_fkey FOREIGN KEY (id_horario) REFERENCES public.horario(id_horario);
 [   ALTER TABLE ONLY public.profesor_horario DROP CONSTRAINT profesor_horario_id_horario_fkey;
       public               postgres    false    222    4684    230            b           2606    16840 2   profesor_horario profesor_horario_id_profesor_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.profesor_horario
    ADD CONSTRAINT profesor_horario_id_profesor_fkey FOREIGN KEY (id_profesor) REFERENCES public.profesor(id_profesor);
 \   ALTER TABLE ONLY public.profesor_horario DROP CONSTRAINT profesor_horario_id_profesor_fkey;
       public               postgres    false    220    4682    230                  x������ � �            x������ � �      �      x������ � �      �      x������ � �            x������ � �            x������ � �            x������ � �      �      x������ � �      �      x������ � �            x������ � �     