"""Initial migration

Revision ID: c56d4243405c
Revises: 35dd8bd8e211
Create Date: 2024-06-16 20:50:26.990819

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c56d4243405c'
down_revision = '35dd8bd8e211'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('report_details', 'date_from',
               existing_type=sa.DATE(),
               type_=sa.String(),
               existing_nullable=True)
    op.alter_column('report_details', 'date_to',
               existing_type=sa.DATE(),
               type_=sa.String(),
               existing_nullable=True)
    op.alter_column('report_details', 'create_dt',
               existing_type=sa.DATE(),
               type_=sa.String(),
               existing_nullable=True)
    op.alter_column('report_details', 'order_dt',
               existing_type=sa.DATE(),
               type_=sa.String(),
               existing_nullable=True)
    op.alter_column('report_details', 'sale_dt',
               existing_type=sa.DATE(),
               type_=sa.String(),
               existing_nullable=True)
    op.alter_column('report_details', 'rr_dt',
               existing_type=sa.DATE(),
               type_=sa.String(),
               existing_nullable=True)
    op.alter_column('report_details', 'delivery_amount',
               existing_type=sa.DOUBLE_PRECISION(precision=53),
               type_=sa.Integer(),
               existing_nullable=True)
    op.alter_column('report_details', 'return_amount',
               existing_type=sa.DOUBLE_PRECISION(precision=53),
               type_=sa.Integer(),
               existing_nullable=True)
    op.alter_column('report_details', 'sticker_id',
               existing_type=sa.INTEGER(),
               type_=sa.String(),
               existing_nullable=True)
    op.alter_column('report_details', 'srid',
               existing_type=sa.INTEGER(),
               type_=sa.String(),
               existing_nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('report_details', 'srid',
               existing_type=sa.String(),
               type_=sa.INTEGER(),
               existing_nullable=True)
    op.alter_column('report_details', 'sticker_id',
               existing_type=sa.String(),
               type_=sa.INTEGER(),
               existing_nullable=True)
    op.alter_column('report_details', 'return_amount',
               existing_type=sa.Integer(),
               type_=sa.DOUBLE_PRECISION(precision=53),
               existing_nullable=True)
    op.alter_column('report_details', 'delivery_amount',
               existing_type=sa.Integer(),
               type_=sa.DOUBLE_PRECISION(precision=53),
               existing_nullable=True)
    op.alter_column('report_details', 'rr_dt',
               existing_type=sa.String(),
               type_=sa.DATE(),
               existing_nullable=True)
    op.alter_column('report_details', 'sale_dt',
               existing_type=sa.String(),
               type_=sa.DATE(),
               existing_nullable=True)
    op.alter_column('report_details', 'order_dt',
               existing_type=sa.String(),
               type_=sa.DATE(),
               existing_nullable=True)
    op.alter_column('report_details', 'create_dt',
               existing_type=sa.String(),
               type_=sa.DATE(),
               existing_nullable=True)
    op.alter_column('report_details', 'date_to',
               existing_type=sa.String(),
               type_=sa.DATE(),
               existing_nullable=True)
    op.alter_column('report_details', 'date_from',
               existing_type=sa.String(),
               type_=sa.DATE(),
               existing_nullable=True)
    # ### end Alembic commands ###
