// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package ec2

import (
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// Provides an EC2 Capacity Reservation. This allows you to reserve capacity for your Amazon EC2 instances in a specific Availability Zone for any duration.
type CapacityReservation struct {
	pulumi.CustomResourceState

	// The Availability Zone in which to create the Capacity Reservation.
	AvailabilityZone pulumi.StringOutput `pulumi:"availabilityZone"`
	// Indicates whether the Capacity Reservation supports EBS-optimized instances.
	EbsOptimized pulumi.BoolPtrOutput `pulumi:"ebsOptimized"`
	// The date and time at which the Capacity Reservation expires. When a Capacity Reservation expires, the reserved capacity is released and you can no longer launch instances into it. Valid values: [RFC3339 time string](https://tools.ietf.org/html/rfc3339#section-5.8) (`YYYY-MM-DDTHH:MM:SSZ`)
	EndDate pulumi.StringPtrOutput `pulumi:"endDate"`
	// Indicates the way in which the Capacity Reservation ends. Specify either `unlimited` or `limited`.
	EndDateType pulumi.StringPtrOutput `pulumi:"endDateType"`
	// Indicates whether the Capacity Reservation supports instances with temporary, block-level storage.
	EphemeralStorage pulumi.BoolPtrOutput `pulumi:"ephemeralStorage"`
	// The number of instances for which to reserve capacity.
	InstanceCount pulumi.IntOutput `pulumi:"instanceCount"`
	// Indicates the type of instance launches that the Capacity Reservation accepts. Specify either `open` or `targeted`.
	InstanceMatchCriteria pulumi.StringPtrOutput `pulumi:"instanceMatchCriteria"`
	// The type of operating system for which to reserve capacity. Valid options are `Linux/UNIX`, `Red Hat Enterprise Linux`, `SUSE Linux`, `Windows`, `Windows with SQL Server`, `Windows with SQL Server Enterprise`, `Windows with SQL Server Standard` or `Windows with SQL Server Web`.
	InstancePlatform pulumi.StringOutput `pulumi:"instancePlatform"`
	// The instance type for which to reserve capacity.
	InstanceType pulumi.StringOutput `pulumi:"instanceType"`
	// A map of tags to assign to the resource.
	Tags pulumi.MapOutput `pulumi:"tags"`
	// Indicates the tenancy of the Capacity Reservation. Specify either `default` or `dedicated`.
	Tenancy pulumi.StringPtrOutput `pulumi:"tenancy"`
}

// NewCapacityReservation registers a new resource with the given unique name, arguments, and options.
func NewCapacityReservation(ctx *pulumi.Context,
	name string, args *CapacityReservationArgs, opts ...pulumi.ResourceOption) (*CapacityReservation, error) {
	if args == nil || args.AvailabilityZone == nil {
		return nil, errors.New("missing required argument 'AvailabilityZone'")
	}
	if args == nil || args.InstanceCount == nil {
		return nil, errors.New("missing required argument 'InstanceCount'")
	}
	if args == nil || args.InstancePlatform == nil {
		return nil, errors.New("missing required argument 'InstancePlatform'")
	}
	if args == nil || args.InstanceType == nil {
		return nil, errors.New("missing required argument 'InstanceType'")
	}
	if args == nil {
		args = &CapacityReservationArgs{}
	}
	var resource CapacityReservation
	err := ctx.RegisterResource("aws:ec2/capacityReservation:CapacityReservation", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetCapacityReservation gets an existing CapacityReservation resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetCapacityReservation(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *CapacityReservationState, opts ...pulumi.ResourceOption) (*CapacityReservation, error) {
	var resource CapacityReservation
	err := ctx.ReadResource("aws:ec2/capacityReservation:CapacityReservation", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering CapacityReservation resources.
type capacityReservationState struct {
	// The Availability Zone in which to create the Capacity Reservation.
	AvailabilityZone *string `pulumi:"availabilityZone"`
	// Indicates whether the Capacity Reservation supports EBS-optimized instances.
	EbsOptimized *bool `pulumi:"ebsOptimized"`
	// The date and time at which the Capacity Reservation expires. When a Capacity Reservation expires, the reserved capacity is released and you can no longer launch instances into it. Valid values: [RFC3339 time string](https://tools.ietf.org/html/rfc3339#section-5.8) (`YYYY-MM-DDTHH:MM:SSZ`)
	EndDate *string `pulumi:"endDate"`
	// Indicates the way in which the Capacity Reservation ends. Specify either `unlimited` or `limited`.
	EndDateType *string `pulumi:"endDateType"`
	// Indicates whether the Capacity Reservation supports instances with temporary, block-level storage.
	EphemeralStorage *bool `pulumi:"ephemeralStorage"`
	// The number of instances for which to reserve capacity.
	InstanceCount *int `pulumi:"instanceCount"`
	// Indicates the type of instance launches that the Capacity Reservation accepts. Specify either `open` or `targeted`.
	InstanceMatchCriteria *string `pulumi:"instanceMatchCriteria"`
	// The type of operating system for which to reserve capacity. Valid options are `Linux/UNIX`, `Red Hat Enterprise Linux`, `SUSE Linux`, `Windows`, `Windows with SQL Server`, `Windows with SQL Server Enterprise`, `Windows with SQL Server Standard` or `Windows with SQL Server Web`.
	InstancePlatform *string `pulumi:"instancePlatform"`
	// The instance type for which to reserve capacity.
	InstanceType *string `pulumi:"instanceType"`
	// A map of tags to assign to the resource.
	Tags map[string]interface{} `pulumi:"tags"`
	// Indicates the tenancy of the Capacity Reservation. Specify either `default` or `dedicated`.
	Tenancy *string `pulumi:"tenancy"`
}

type CapacityReservationState struct {
	// The Availability Zone in which to create the Capacity Reservation.
	AvailabilityZone pulumi.StringPtrInput
	// Indicates whether the Capacity Reservation supports EBS-optimized instances.
	EbsOptimized pulumi.BoolPtrInput
	// The date and time at which the Capacity Reservation expires. When a Capacity Reservation expires, the reserved capacity is released and you can no longer launch instances into it. Valid values: [RFC3339 time string](https://tools.ietf.org/html/rfc3339#section-5.8) (`YYYY-MM-DDTHH:MM:SSZ`)
	EndDate pulumi.StringPtrInput
	// Indicates the way in which the Capacity Reservation ends. Specify either `unlimited` or `limited`.
	EndDateType pulumi.StringPtrInput
	// Indicates whether the Capacity Reservation supports instances with temporary, block-level storage.
	EphemeralStorage pulumi.BoolPtrInput
	// The number of instances for which to reserve capacity.
	InstanceCount pulumi.IntPtrInput
	// Indicates the type of instance launches that the Capacity Reservation accepts. Specify either `open` or `targeted`.
	InstanceMatchCriteria pulumi.StringPtrInput
	// The type of operating system for which to reserve capacity. Valid options are `Linux/UNIX`, `Red Hat Enterprise Linux`, `SUSE Linux`, `Windows`, `Windows with SQL Server`, `Windows with SQL Server Enterprise`, `Windows with SQL Server Standard` or `Windows with SQL Server Web`.
	InstancePlatform pulumi.StringPtrInput
	// The instance type for which to reserve capacity.
	InstanceType pulumi.StringPtrInput
	// A map of tags to assign to the resource.
	Tags pulumi.MapInput
	// Indicates the tenancy of the Capacity Reservation. Specify either `default` or `dedicated`.
	Tenancy pulumi.StringPtrInput
}

func (CapacityReservationState) ElementType() reflect.Type {
	return reflect.TypeOf((*capacityReservationState)(nil)).Elem()
}

type capacityReservationArgs struct {
	// The Availability Zone in which to create the Capacity Reservation.
	AvailabilityZone string `pulumi:"availabilityZone"`
	// Indicates whether the Capacity Reservation supports EBS-optimized instances.
	EbsOptimized *bool `pulumi:"ebsOptimized"`
	// The date and time at which the Capacity Reservation expires. When a Capacity Reservation expires, the reserved capacity is released and you can no longer launch instances into it. Valid values: [RFC3339 time string](https://tools.ietf.org/html/rfc3339#section-5.8) (`YYYY-MM-DDTHH:MM:SSZ`)
	EndDate *string `pulumi:"endDate"`
	// Indicates the way in which the Capacity Reservation ends. Specify either `unlimited` or `limited`.
	EndDateType *string `pulumi:"endDateType"`
	// Indicates whether the Capacity Reservation supports instances with temporary, block-level storage.
	EphemeralStorage *bool `pulumi:"ephemeralStorage"`
	// The number of instances for which to reserve capacity.
	InstanceCount int `pulumi:"instanceCount"`
	// Indicates the type of instance launches that the Capacity Reservation accepts. Specify either `open` or `targeted`.
	InstanceMatchCriteria *string `pulumi:"instanceMatchCriteria"`
	// The type of operating system for which to reserve capacity. Valid options are `Linux/UNIX`, `Red Hat Enterprise Linux`, `SUSE Linux`, `Windows`, `Windows with SQL Server`, `Windows with SQL Server Enterprise`, `Windows with SQL Server Standard` or `Windows with SQL Server Web`.
	InstancePlatform string `pulumi:"instancePlatform"`
	// The instance type for which to reserve capacity.
	InstanceType string `pulumi:"instanceType"`
	// A map of tags to assign to the resource.
	Tags map[string]interface{} `pulumi:"tags"`
	// Indicates the tenancy of the Capacity Reservation. Specify either `default` or `dedicated`.
	Tenancy *string `pulumi:"tenancy"`
}

// The set of arguments for constructing a CapacityReservation resource.
type CapacityReservationArgs struct {
	// The Availability Zone in which to create the Capacity Reservation.
	AvailabilityZone pulumi.StringInput
	// Indicates whether the Capacity Reservation supports EBS-optimized instances.
	EbsOptimized pulumi.BoolPtrInput
	// The date and time at which the Capacity Reservation expires. When a Capacity Reservation expires, the reserved capacity is released and you can no longer launch instances into it. Valid values: [RFC3339 time string](https://tools.ietf.org/html/rfc3339#section-5.8) (`YYYY-MM-DDTHH:MM:SSZ`)
	EndDate pulumi.StringPtrInput
	// Indicates the way in which the Capacity Reservation ends. Specify either `unlimited` or `limited`.
	EndDateType pulumi.StringPtrInput
	// Indicates whether the Capacity Reservation supports instances with temporary, block-level storage.
	EphemeralStorage pulumi.BoolPtrInput
	// The number of instances for which to reserve capacity.
	InstanceCount pulumi.IntInput
	// Indicates the type of instance launches that the Capacity Reservation accepts. Specify either `open` or `targeted`.
	InstanceMatchCriteria pulumi.StringPtrInput
	// The type of operating system for which to reserve capacity. Valid options are `Linux/UNIX`, `Red Hat Enterprise Linux`, `SUSE Linux`, `Windows`, `Windows with SQL Server`, `Windows with SQL Server Enterprise`, `Windows with SQL Server Standard` or `Windows with SQL Server Web`.
	InstancePlatform pulumi.StringInput
	// The instance type for which to reserve capacity.
	InstanceType pulumi.StringInput
	// A map of tags to assign to the resource.
	Tags pulumi.MapInput
	// Indicates the tenancy of the Capacity Reservation. Specify either `default` or `dedicated`.
	Tenancy pulumi.StringPtrInput
}

func (CapacityReservationArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*capacityReservationArgs)(nil)).Elem()
}
