// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

// nolint: lll
package dynamodb

import (
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// Provides a DynamoDB table item resource
//
// > **Note:** This resource is not meant to be used for managing large amounts of data in your table, it is not designed to scale.
//   You should perform **regular backups** of all data in the table, see [AWS docs for more](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/BackupRestore.html).
//
//
//
// > This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/dynamodb_table_item.html.markdown.
type TableItem struct {
	pulumi.CustomResourceState

	// Hash key to use for lookups and identification of the item
	HashKey pulumi.StringOutput `pulumi:"hashKey"`
	// JSON representation of a map of attribute name/value pairs, one for each attribute.
	// Only the primary key attributes are required; you can optionally provide other attribute name-value pairs for the item.
	Item pulumi.StringOutput `pulumi:"item"`
	// Range key to use for lookups and identification of the item. Required if there is range key defined in the table.
	RangeKey pulumi.StringPtrOutput `pulumi:"rangeKey"`
	// The name of the table to contain the item.
	TableName pulumi.StringOutput `pulumi:"tableName"`
}

// NewTableItem registers a new resource with the given unique name, arguments, and options.
func NewTableItem(ctx *pulumi.Context,
	name string, args *TableItemArgs, opts ...pulumi.ResourceOption) (*TableItem, error) {
	if args == nil || args.HashKey == nil {
		return nil, errors.New("missing required argument 'HashKey'")
	}
	if args == nil || args.Item == nil {
		return nil, errors.New("missing required argument 'Item'")
	}
	if args == nil || args.TableName == nil {
		return nil, errors.New("missing required argument 'TableName'")
	}
	if args == nil {
		args = &TableItemArgs{}
	}
	var resource TableItem
	err := ctx.RegisterResource("aws:dynamodb/tableItem:TableItem", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetTableItem gets an existing TableItem resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetTableItem(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *TableItemState, opts ...pulumi.ResourceOption) (*TableItem, error) {
	var resource TableItem
	err := ctx.ReadResource("aws:dynamodb/tableItem:TableItem", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering TableItem resources.
type tableItemState struct {
	// Hash key to use for lookups and identification of the item
	HashKey *string `pulumi:"hashKey"`
	// JSON representation of a map of attribute name/value pairs, one for each attribute.
	// Only the primary key attributes are required; you can optionally provide other attribute name-value pairs for the item.
	Item *string `pulumi:"item"`
	// Range key to use for lookups and identification of the item. Required if there is range key defined in the table.
	RangeKey *string `pulumi:"rangeKey"`
	// The name of the table to contain the item.
	TableName *string `pulumi:"tableName"`
}

type TableItemState struct {
	// Hash key to use for lookups and identification of the item
	HashKey pulumi.StringPtrInput
	// JSON representation of a map of attribute name/value pairs, one for each attribute.
	// Only the primary key attributes are required; you can optionally provide other attribute name-value pairs for the item.
	Item pulumi.StringPtrInput
	// Range key to use for lookups and identification of the item. Required if there is range key defined in the table.
	RangeKey pulumi.StringPtrInput
	// The name of the table to contain the item.
	TableName pulumi.StringPtrInput
}

func (TableItemState) ElementType() reflect.Type {
	return reflect.TypeOf((*tableItemState)(nil)).Elem()
}

type tableItemArgs struct {
	// Hash key to use for lookups and identification of the item
	HashKey string `pulumi:"hashKey"`
	// JSON representation of a map of attribute name/value pairs, one for each attribute.
	// Only the primary key attributes are required; you can optionally provide other attribute name-value pairs for the item.
	Item string `pulumi:"item"`
	// Range key to use for lookups and identification of the item. Required if there is range key defined in the table.
	RangeKey *string `pulumi:"rangeKey"`
	// The name of the table to contain the item.
	TableName string `pulumi:"tableName"`
}

// The set of arguments for constructing a TableItem resource.
type TableItemArgs struct {
	// Hash key to use for lookups and identification of the item
	HashKey pulumi.StringInput
	// JSON representation of a map of attribute name/value pairs, one for each attribute.
	// Only the primary key attributes are required; you can optionally provide other attribute name-value pairs for the item.
	Item pulumi.StringInput
	// Range key to use for lookups and identification of the item. Required if there is range key defined in the table.
	RangeKey pulumi.StringPtrInput
	// The name of the table to contain the item.
	TableName pulumi.StringInput
}

func (TableItemArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*tableItemArgs)(nil)).Elem()
}
