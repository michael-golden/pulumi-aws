// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

// nolint: lll
package redshift

import (
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

//
//
// > This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/redshift_snapshot_schedule_association.html.markdown.
type SnapshotScheduleAssociation struct {
	pulumi.CustomResourceState

	// The cluster identifier.
	ClusterIdentifier pulumi.StringOutput `pulumi:"clusterIdentifier"`
	// The snapshot schedule identifier.
	ScheduleIdentifier pulumi.StringOutput `pulumi:"scheduleIdentifier"`
}

// NewSnapshotScheduleAssociation registers a new resource with the given unique name, arguments, and options.
func NewSnapshotScheduleAssociation(ctx *pulumi.Context,
	name string, args *SnapshotScheduleAssociationArgs, opts ...pulumi.ResourceOption) (*SnapshotScheduleAssociation, error) {
	if args == nil || args.ClusterIdentifier == nil {
		return nil, errors.New("missing required argument 'ClusterIdentifier'")
	}
	if args == nil || args.ScheduleIdentifier == nil {
		return nil, errors.New("missing required argument 'ScheduleIdentifier'")
	}
	if args == nil {
		args = &SnapshotScheduleAssociationArgs{}
	}
	var resource SnapshotScheduleAssociation
	err := ctx.RegisterResource("aws:redshift/snapshotScheduleAssociation:SnapshotScheduleAssociation", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetSnapshotScheduleAssociation gets an existing SnapshotScheduleAssociation resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetSnapshotScheduleAssociation(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *SnapshotScheduleAssociationState, opts ...pulumi.ResourceOption) (*SnapshotScheduleAssociation, error) {
	var resource SnapshotScheduleAssociation
	err := ctx.ReadResource("aws:redshift/snapshotScheduleAssociation:SnapshotScheduleAssociation", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering SnapshotScheduleAssociation resources.
type snapshotScheduleAssociationState struct {
	// The cluster identifier.
	ClusterIdentifier *string `pulumi:"clusterIdentifier"`
	// The snapshot schedule identifier.
	ScheduleIdentifier *string `pulumi:"scheduleIdentifier"`
}

type SnapshotScheduleAssociationState struct {
	// The cluster identifier.
	ClusterIdentifier pulumi.StringPtrInput
	// The snapshot schedule identifier.
	ScheduleIdentifier pulumi.StringPtrInput
}

func (SnapshotScheduleAssociationState) ElementType() reflect.Type {
	return reflect.TypeOf((*snapshotScheduleAssociationState)(nil)).Elem()
}

type snapshotScheduleAssociationArgs struct {
	// The cluster identifier.
	ClusterIdentifier string `pulumi:"clusterIdentifier"`
	// The snapshot schedule identifier.
	ScheduleIdentifier string `pulumi:"scheduleIdentifier"`
}

// The set of arguments for constructing a SnapshotScheduleAssociation resource.
type SnapshotScheduleAssociationArgs struct {
	// The cluster identifier.
	ClusterIdentifier pulumi.StringInput
	// The snapshot schedule identifier.
	ScheduleIdentifier pulumi.StringInput
}

func (SnapshotScheduleAssociationArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*snapshotScheduleAssociationArgs)(nil)).Elem()
}
