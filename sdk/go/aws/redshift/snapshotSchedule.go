// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package redshift

import (
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

type SnapshotSchedule struct {
	pulumi.CustomResourceState

	Arn pulumi.StringOutput `pulumi:"arn"`
	// The definition of the snapshot schedule. The definition is made up of schedule expressions, for example `cron(30 12 *)` or `rate(12 hours)`.
	Definitions pulumi.StringArrayOutput `pulumi:"definitions"`
	// The description of the snapshot schedule.
	Description pulumi.StringPtrOutput `pulumi:"description"`
	// Whether to destroy all associated clusters with this snapshot schedule on deletion. Must be enabled and applied before attempting deletion.
	ForceDestroy pulumi.BoolPtrOutput `pulumi:"forceDestroy"`
	// The snapshot schedule identifier. If omitted, this provider will assign a random, unique identifier.
	Identifier pulumi.StringOutput `pulumi:"identifier"`
	// Creates a unique
	// identifier beginning with the specified prefix. Conflicts with `identifier`.
	IdentifierPrefix pulumi.StringOutput `pulumi:"identifierPrefix"`
	// A map of tags to assign to the resource.
	Tags pulumi.MapOutput `pulumi:"tags"`
}

// NewSnapshotSchedule registers a new resource with the given unique name, arguments, and options.
func NewSnapshotSchedule(ctx *pulumi.Context,
	name string, args *SnapshotScheduleArgs, opts ...pulumi.ResourceOption) (*SnapshotSchedule, error) {
	if args == nil || args.Definitions == nil {
		return nil, errors.New("missing required argument 'Definitions'")
	}
	if args == nil {
		args = &SnapshotScheduleArgs{}
	}
	var resource SnapshotSchedule
	err := ctx.RegisterResource("aws:redshift/snapshotSchedule:SnapshotSchedule", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetSnapshotSchedule gets an existing SnapshotSchedule resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetSnapshotSchedule(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *SnapshotScheduleState, opts ...pulumi.ResourceOption) (*SnapshotSchedule, error) {
	var resource SnapshotSchedule
	err := ctx.ReadResource("aws:redshift/snapshotSchedule:SnapshotSchedule", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering SnapshotSchedule resources.
type snapshotScheduleState struct {
	Arn *string `pulumi:"arn"`
	// The definition of the snapshot schedule. The definition is made up of schedule expressions, for example `cron(30 12 *)` or `rate(12 hours)`.
	Definitions []string `pulumi:"definitions"`
	// The description of the snapshot schedule.
	Description *string `pulumi:"description"`
	// Whether to destroy all associated clusters with this snapshot schedule on deletion. Must be enabled and applied before attempting deletion.
	ForceDestroy *bool `pulumi:"forceDestroy"`
	// The snapshot schedule identifier. If omitted, this provider will assign a random, unique identifier.
	Identifier *string `pulumi:"identifier"`
	// Creates a unique
	// identifier beginning with the specified prefix. Conflicts with `identifier`.
	IdentifierPrefix *string `pulumi:"identifierPrefix"`
	// A map of tags to assign to the resource.
	Tags map[string]interface{} `pulumi:"tags"`
}

type SnapshotScheduleState struct {
	Arn pulumi.StringPtrInput
	// The definition of the snapshot schedule. The definition is made up of schedule expressions, for example `cron(30 12 *)` or `rate(12 hours)`.
	Definitions pulumi.StringArrayInput
	// The description of the snapshot schedule.
	Description pulumi.StringPtrInput
	// Whether to destroy all associated clusters with this snapshot schedule on deletion. Must be enabled and applied before attempting deletion.
	ForceDestroy pulumi.BoolPtrInput
	// The snapshot schedule identifier. If omitted, this provider will assign a random, unique identifier.
	Identifier pulumi.StringPtrInput
	// Creates a unique
	// identifier beginning with the specified prefix. Conflicts with `identifier`.
	IdentifierPrefix pulumi.StringPtrInput
	// A map of tags to assign to the resource.
	Tags pulumi.MapInput
}

func (SnapshotScheduleState) ElementType() reflect.Type {
	return reflect.TypeOf((*snapshotScheduleState)(nil)).Elem()
}

type snapshotScheduleArgs struct {
	// The definition of the snapshot schedule. The definition is made up of schedule expressions, for example `cron(30 12 *)` or `rate(12 hours)`.
	Definitions []string `pulumi:"definitions"`
	// The description of the snapshot schedule.
	Description *string `pulumi:"description"`
	// Whether to destroy all associated clusters with this snapshot schedule on deletion. Must be enabled and applied before attempting deletion.
	ForceDestroy *bool `pulumi:"forceDestroy"`
	// The snapshot schedule identifier. If omitted, this provider will assign a random, unique identifier.
	Identifier *string `pulumi:"identifier"`
	// Creates a unique
	// identifier beginning with the specified prefix. Conflicts with `identifier`.
	IdentifierPrefix *string `pulumi:"identifierPrefix"`
	// A map of tags to assign to the resource.
	Tags map[string]interface{} `pulumi:"tags"`
}

// The set of arguments for constructing a SnapshotSchedule resource.
type SnapshotScheduleArgs struct {
	// The definition of the snapshot schedule. The definition is made up of schedule expressions, for example `cron(30 12 *)` or `rate(12 hours)`.
	Definitions pulumi.StringArrayInput
	// The description of the snapshot schedule.
	Description pulumi.StringPtrInput
	// Whether to destroy all associated clusters with this snapshot schedule on deletion. Must be enabled and applied before attempting deletion.
	ForceDestroy pulumi.BoolPtrInput
	// The snapshot schedule identifier. If omitted, this provider will assign a random, unique identifier.
	Identifier pulumi.StringPtrInput
	// Creates a unique
	// identifier beginning with the specified prefix. Conflicts with `identifier`.
	IdentifierPrefix pulumi.StringPtrInput
	// A map of tags to assign to the resource.
	Tags pulumi.MapInput
}

func (SnapshotScheduleArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*snapshotScheduleArgs)(nil)).Elem()
}
