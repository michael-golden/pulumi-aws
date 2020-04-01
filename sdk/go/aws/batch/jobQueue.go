// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

// nolint: lll
package batch

import (
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// Provides a Batch Job Queue resource.
//
//
//
// > This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/batch_job_queue.html.markdown.
type JobQueue struct {
	pulumi.CustomResourceState

	// The Amazon Resource Name of the job queue.
	Arn pulumi.StringOutput `pulumi:"arn"`
	// Specifies the set of compute environments
	// mapped to a job queue and their order.  The position of the compute environments
	// in the list will dictate the order. You can associate up to 3 compute environments
	// with a job queue.
	ComputeEnvironments pulumi.StringArrayOutput `pulumi:"computeEnvironments"`
	// Specifies the name of the job queue.
	Name pulumi.StringOutput `pulumi:"name"`
	// The priority of the job queue. Job queues with a higher priority
	// are evaluated first when associated with the same compute environment.
	Priority pulumi.IntOutput `pulumi:"priority"`
	// The state of the job queue. Must be one of: `ENABLED` or `DISABLED`
	State pulumi.StringOutput `pulumi:"state"`
}

// NewJobQueue registers a new resource with the given unique name, arguments, and options.
func NewJobQueue(ctx *pulumi.Context,
	name string, args *JobQueueArgs, opts ...pulumi.ResourceOption) (*JobQueue, error) {
	if args == nil || args.ComputeEnvironments == nil {
		return nil, errors.New("missing required argument 'ComputeEnvironments'")
	}
	if args == nil || args.Priority == nil {
		return nil, errors.New("missing required argument 'Priority'")
	}
	if args == nil || args.State == nil {
		return nil, errors.New("missing required argument 'State'")
	}
	if args == nil {
		args = &JobQueueArgs{}
	}
	var resource JobQueue
	err := ctx.RegisterResource("aws:batch/jobQueue:JobQueue", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetJobQueue gets an existing JobQueue resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetJobQueue(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *JobQueueState, opts ...pulumi.ResourceOption) (*JobQueue, error) {
	var resource JobQueue
	err := ctx.ReadResource("aws:batch/jobQueue:JobQueue", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering JobQueue resources.
type jobQueueState struct {
	// The Amazon Resource Name of the job queue.
	Arn *string `pulumi:"arn"`
	// Specifies the set of compute environments
	// mapped to a job queue and their order.  The position of the compute environments
	// in the list will dictate the order. You can associate up to 3 compute environments
	// with a job queue.
	ComputeEnvironments []string `pulumi:"computeEnvironments"`
	// Specifies the name of the job queue.
	Name *string `pulumi:"name"`
	// The priority of the job queue. Job queues with a higher priority
	// are evaluated first when associated with the same compute environment.
	Priority *int `pulumi:"priority"`
	// The state of the job queue. Must be one of: `ENABLED` or `DISABLED`
	State *string `pulumi:"state"`
}

type JobQueueState struct {
	// The Amazon Resource Name of the job queue.
	Arn pulumi.StringPtrInput
	// Specifies the set of compute environments
	// mapped to a job queue and their order.  The position of the compute environments
	// in the list will dictate the order. You can associate up to 3 compute environments
	// with a job queue.
	ComputeEnvironments pulumi.StringArrayInput
	// Specifies the name of the job queue.
	Name pulumi.StringPtrInput
	// The priority of the job queue. Job queues with a higher priority
	// are evaluated first when associated with the same compute environment.
	Priority pulumi.IntPtrInput
	// The state of the job queue. Must be one of: `ENABLED` or `DISABLED`
	State pulumi.StringPtrInput
}

func (JobQueueState) ElementType() reflect.Type {
	return reflect.TypeOf((*jobQueueState)(nil)).Elem()
}

type jobQueueArgs struct {
	// Specifies the set of compute environments
	// mapped to a job queue and their order.  The position of the compute environments
	// in the list will dictate the order. You can associate up to 3 compute environments
	// with a job queue.
	ComputeEnvironments []string `pulumi:"computeEnvironments"`
	// Specifies the name of the job queue.
	Name *string `pulumi:"name"`
	// The priority of the job queue. Job queues with a higher priority
	// are evaluated first when associated with the same compute environment.
	Priority int `pulumi:"priority"`
	// The state of the job queue. Must be one of: `ENABLED` or `DISABLED`
	State string `pulumi:"state"`
}

// The set of arguments for constructing a JobQueue resource.
type JobQueueArgs struct {
	// Specifies the set of compute environments
	// mapped to a job queue and their order.  The position of the compute environments
	// in the list will dictate the order. You can associate up to 3 compute environments
	// with a job queue.
	ComputeEnvironments pulumi.StringArrayInput
	// Specifies the name of the job queue.
	Name pulumi.StringPtrInput
	// The priority of the job queue. Job queues with a higher priority
	// are evaluated first when associated with the same compute environment.
	Priority pulumi.IntInput
	// The state of the job queue. Must be one of: `ENABLED` or `DISABLED`
	State pulumi.StringInput
}

func (JobQueueArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*jobQueueArgs)(nil)).Elem()
}
